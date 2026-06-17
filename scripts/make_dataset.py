"""
make_dataset.py
---------------
Generates ALL the raw data for this portfolio project as a small set of LINKED
tables (a mini "data warehouse"), so every data-analysis skill can be practised:
joins, window functions, A/B testing, segmentation, regression, time series, etc.

You normally do NOT need to run this — the CSVs it produces are already committed.
It is here so you (and your instructor) can see how the data was built and
regenerate it if needed. The messiness is DELIBERATE — cleaning it is your job.

Tables produced (in data/raw/):
  customers_raw.csv   one row per customer            (messy)
  products.csv        clean reference list of products
  orders_raw.csv      one row per order  (FK -> customer, product)  (messy)
  returns.csv         orders that were returned       (FK -> order)
  ab_test.csv         marketing experiment per customer (FK -> customer)

See data/DATA_DICTIONARY.md for the full column descriptions and the table diagram.
"""

import csv
import random

random.seed(42)  # fixed seed => identical files every run

RAW = "data/raw"

# --------------------------------------------------------------------------
# helpers to make values messy on purpose
# --------------------------------------------------------------------------
def messy_phone():
    n = "7" + "".join(random.choice("0123456789") for _ in range(8))
    style = random.choice(["07", "+254", "254", "7"])
    return {"07": "0" + n, "+254": "+254" + n, "254": "254" + n, "7": n}[style]

def messy_date(y, m, d):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    style = random.choice(["iso", "slash", "text"])
    if style == "iso":   return f"{y:04d}-{m:02d}-{d:02d}"
    if style == "slash": return f"{d:02d}/{m:02d}/{y:04d}"
    return f"{months[m-1]} {d} {y}"

def messy_name(fn, ln):
    name = f"{fn} {ln}"
    return random.choice([name, name.lower(), name.upper(), f"  {name} ", f"{fn}  {ln}"])

def messy_county(c):
    if c == "Nairobi": return random.choice(["Nairobi","nairobi","NAIROBI"," Nairobi"])
    if c == "Mombasa": return random.choice(["Mombasa","Mombassa","mombasa"])
    return random.choice([c, c.lower(), c + " "])

def messy_choice(variants):
    return random.choice(variants)

first_names = ["Brian","Amina","John","Faith","Kevin","Mercy","Daniel","Grace",
               "Samuel","Joyce","Peter","Wanjiru","Otieno","Halima","Collins",
               "Esther","Victor","Nasra","Dennis","Lucy","Alice","Mohamed",
               "Caroline","James","Zainab","Eric","Naomi","Brenda","Tony","Ruth"]
last_names = ["Mwangi","Otieno","Kamau","Achieng","Mutua","Wafula","Chebet",
              "Njoroge","Abdi","Kiprono","Omondi","Were","Mwende","Barasa"]
counties = ["Nairobi","Mombasa","Kisumu","Nakuru","Eldoret","Thika"]

# --------------------------------------------------------------------------
# 1. PRODUCTS  (clean reference table)
# --------------------------------------------------------------------------
# product_id, name, category, cost_price (what we pay), list_price (what we charge)
product_defs = [
    ("Wireless Earbuds","Electronics",2100,3500), ("Phone Charger","Electronics",350,800),
    ("Bluetooth Speaker","Electronics",1500,2500), ("Power Bank","Electronics",1100,1800),
    ("Smart Watch","Electronics",3200,5200), ("USB Cable","Electronics",120,300),
    ("Cotton T-Shirt","Clothing",450,950), ("Denim Jeans","Clothing",1300,2200),
    ("Sports Shoes","Clothing",2600,4200), ("Leather Belt","Clothing",300,700),
    ("Hoodie","Clothing",1100,1900),
    ("Notebook Set","Stationery",150,350), ("Ballpoint Pens","Stationery",80,200),
    ("Backpack","Stationery",900,1600), ("Calculator","Stationery",400,750),
    ("Frying Pan","Home",650,1200), ("Bedsheet Set","Home",1500,2800),
    ("Water Bottle","Home",250,600), ("Table Lamp","Home",800,1500),
    ("Wall Clock","Home",500,1100),
]
products = []
for i, (name, cat, cost, lp) in enumerate(product_defs, start=1):
    products.append({"product_id": f"P{i:02d}", "product_name": name,
                     "category": cat, "cost_price": cost, "list_price": lp})

with open(f"{RAW}/products.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["product_id","product_name","category","cost_price","list_price"])
    w.writeheader(); w.writerows(products)

# --------------------------------------------------------------------------
# 2. CUSTOMERS  (messy)
# --------------------------------------------------------------------------
N_CUST = 300
customers = []
for i in range(1, N_CUST + 1):
    fn, ln = random.choice(first_names), random.choice(last_names)
    age = random.randint(18, 65)
    # inject a few impossible ages to be cleaned as outliers
    if random.random() < 0.03: age = random.choice([0, 5, 150, 200])
    customers.append({
        "customer_id": f"C{i:04d}",
        "name": messy_name(fn, ln),
        "phone": messy_phone(),
        "county": messy_county(random.choice(counties)),
        "gender": messy_choice(["M","F","Male","Female","m","f"]),
        "age": age,
        "signup_date": messy_date(random.choice([2023,2024]), random.randint(1,12), random.randint(1,28)),
    })
# blank some genders/counties
for c in random.sample(customers, 12): c["county"] = ""
for c in random.sample(customers, 9):  c["gender"] = ""

with open(f"{RAW}/customers_raw.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["customer_id","name","phone","county","gender","age","signup_date"])
    w.writeheader(); w.writerows(customers)

# --------------------------------------------------------------------------
# 3. ORDERS  (messy)  spread across 18 months for time-series analysis
# --------------------------------------------------------------------------
def messy_price(p):
    style = random.choice(["plain","kes","comma","plain"])
    if style == "plain": return str(p)
    if style == "kes":   return f"KES {p}"
    return f"{p:,}"

months_seq = [(2024, m) for m in range(1,13)] + [(2025, m) for m in range(1,7)]  # Jan24..Jun25
orders = []
oid = 10000
for _ in range(2000):
    cust = random.choice(customers)
    prod = random.choice(products)
    y, m = random.choice(months_seq)
    # gentle upward sales trend + a December spike for seasonality
    base_qty = random.choices([1,2,3,4,5], weights=[40,30,15,10,5])[0]
    if m == 12: base_qty += random.choice([0,1,2])          # holiday bump
    qty = base_qty
    if random.random() < 0.015: qty = random.choice([40, 60, 100])  # outliers to detect
    # price near list price with a discount sometimes
    discount = random.choices([0, 0.05, 0.10, 0.15], weights=[60,20,12,8])[0]
    unit = int(prod["list_price"] * (1 - discount))
    # rating has a MILD, discoverable signal: bigger discounts make customers
    # a little happier, very pricey items a little less so, plus random noise.
    score = 3.6 + discount * 5 - (prod["list_price"] / 9000) + random.gauss(0, 0.8)
    rating = max(1, min(5, round(score)))
    orders.append({
        "order_id": f"ORD{oid}",
        "customer_id": cust["customer_id"],
        "product_id": prod["product_id"],
        "order_date": messy_date(y, m, random.randint(1,28)),
        "quantity": qty,
        "unit_price": messy_price(unit),
        "discount": discount,
        "payment_method": messy_choice(["M-Pesa","Mpesa","mpesa","Card","card","Cash","cash"]),
        "channel": messy_choice(["Web","web","App","app","Store","store"]),
        "rating": rating,
    })
    oid += 1
# blank some ratings; inject duplicate rows
for o in random.sample(orders, 120): o["rating"] = ""
for o in random.sample(orders, 40):  orders.append(dict(o))
random.shuffle(orders)

with open(f"{RAW}/orders_raw.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["order_id","customer_id","product_id","order_date",
                                      "quantity","unit_price","discount","payment_method",
                                      "channel","rating"])
    w.writeheader(); w.writerows(orders)

# --------------------------------------------------------------------------
# 4. RETURNS  (~8% of unique orders)
# --------------------------------------------------------------------------
unique_orders = {o["order_id"]: o for o in orders}.values()
returns = []
rid = 500
for o in unique_orders:
    if random.random() < 0.08:
        returns.append({
            "return_id": f"RET{rid}",
            "order_id": o["order_id"],
            "return_date": o["order_date"],   # student can derive days-to-return after cleaning
            "reason": messy_choice(["Damaged","damaged","Wrong item","wrong item",
                                    "Changed mind","Late delivery","Faulty"]),
        })
        rid += 1
with open(f"{RAW}/returns.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["return_id","order_id","return_date","reason"])
    w.writeheader(); w.writerows(returns)

# --------------------------------------------------------------------------
# 5. AB_TEST  (marketing experiment: variant B should convert better)
# --------------------------------------------------------------------------
# exposed customers split into control (A) and treatment (B).
# converted depends on variant + age => good for A/B test AND logistic regression.
exposed = random.sample(customers, 280)
ab = []
for c in exposed:
    variant = random.choice(["A","B"])
    age = c["age"] if isinstance(c["age"], int) else 30
    base = 0.16 if variant == "A" else 0.36      # treatment clearly lifts conversion
    if 25 <= age <= 45: base += 0.05             # mid-age converts a bit more
    converted = 1 if random.random() < base else 0
    ab.append({
        "customer_id": c["customer_id"],
        "variant": variant,
        "exposed_date": messy_date(2025, random.randint(1,5), random.randint(1,28)),
        "converted": converted,
    })
with open(f"{RAW}/ab_test.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["customer_id","variant","exposed_date","converted"])
    w.writeheader(); w.writerows(ab)

print("Generated raw tables in", RAW)
print(f"  products.csv       {len(products)} rows")
print(f"  customers_raw.csv  {len(customers)} rows")
print(f"  orders_raw.csv     {len(orders)} rows (incl. duplicates)")
print(f"  returns.csv        {len(returns)} rows")
print(f"  ab_test.csv        {len(ab)} rows")
