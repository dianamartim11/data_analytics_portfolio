"""
make_dataset.py
---------------
Generates the RAW, intentionally-messy dataset for this portfolio project.

You normally do NOT need to run this — the file it produces,
`data/raw/online_orders_messy.csv`, is already committed for you.
It is here only so you (and your instructor) can see how the messy data
was created, and so it can be regenerated if needed.

The messiness is deliberate. Your job in the project is to CLEAN it.
Known problems baked in on purpose:
  * order_date stored in 3 different formats
  * customer_name has stray spaces and inconsistent capitalisation
  * phone numbers in 4 different formats (07.., +2547.., 2547.., 7..)
  * county spelled inconsistently (Nairobi / nairobi / NAIROBI / Mombasa / Mombassa)
  * category has trailing spaces and singular/plural variants
  * unit_price sometimes has a "KES" label and thousands commas
  * payment_method has casing variants (M-Pesa / Mpesa / mpesa)
  * some rows are exact duplicates
  * some rating and county values are missing (blank)
"""

import csv
import random

random.seed(42)  # fixed seed => the file is identical every time it is generated

OUT = "data/raw/online_orders_messy.csv"

first_names = ["Brian", "Amina", "John", "Faith", "Kevin", "Mercy", "Daniel",
               "Grace", "Samuel", "Joyce", "Peter", "Wanjiru", "Otieno",
               "Halima", "Collins", "Esther", "Victor", "Nasra", "Dennis", "Lucy"]
last_names = ["Mwangi", "Otieno", "Kamau", "Achieng", "Mutua", "Wafula",
              "Chebet", "Njoroge", "Abdi", "Kiprono", "Omondi", "Were"]

# product -> (category, base_price KES)
catalog = {
    "Wireless Earbuds":   ("Electronics", 3500),
    "Phone Charger":      ("Electronics", 800),
    "Bluetooth Speaker":  ("Electronics", 2500),
    "Power Bank":         ("Electronics", 1800),
    "Cotton T-Shirt":     ("Clothing", 950),
    "Denim Jeans":        ("Clothing", 2200),
    "Sports Shoes":       ("Clothing", 4200),
    "Leather Belt":       ("Clothing", 700),
    "Notebook Set":       ("Stationery", 350),
    "Ballpoint Pens":     ("Stationery", 200),
    "Backpack":           ("Stationery", 1600),
    "Frying Pan":         ("Home", 1200),
    "Bedsheet Set":       ("Home", 2800),
    "Water Bottle":       ("Home", 600),
}
products = list(catalog.keys())

counties_clean = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Thika"]

def messy_county(c):
    if c == "Nairobi":
        return random.choice(["Nairobi", "nairobi", "NAIROBI", " Nairobi"])
    if c == "Mombasa":
        return random.choice(["Mombasa", "Mombassa", "mombasa"])
    return random.choice([c, c.lower(), c + " "])

def messy_phone():
    n = "7" + "".join(random.choice("0123456789") for _ in range(8))
    style = random.choice(["07", "+254", "254", "7"])
    if style == "07":
        return "0" + n
    if style == "+254":
        return "+254" + n
    if style == "254":
        return "254" + n
    return n

def messy_date(y, m, d):
    style = random.choice(["iso", "slash", "text"])
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if style == "iso":
        return f"{y:04d}-{m:02d}-{d:02d}"
    if style == "slash":
        return f"{d:02d}/{m:02d}/{y:04d}"
    return f"{months[m-1]} {d} {y}"

def messy_category(cat):
    variants = {
        "Electronics": ["Electronics", "electronics", "Electronics ", "Electronic"],
        "Clothing":    ["Clothing", "clothing", "Clothing ", "Clothes"],
        "Stationery":  ["Stationery", "stationery", "Stationery "],
        "Home":        ["Home", "home", "Home "],
    }
    return random.choice(variants[cat])

def messy_price(p):
    style = random.choice(["plain", "kes", "comma"])
    if style == "plain":
        return str(p)
    if style == "kes":
        return f"KES {p}"
    return f"{p:,}"  # thousands comma e.g. 3,500

def messy_payment():
    return random.choice(["M-Pesa", "Mpesa", "mpesa", "Card", "card", "Cash", "cash"])

rows = []
oid = 1000
for _ in range(220):
    fn = random.choice(first_names)
    ln = random.choice(last_names)
    # add stray spaces / casing to the name sometimes
    name = f"{fn} {ln}"
    name = random.choice([name, name.lower(), name.upper(), f"  {name} ", f"{fn}  {ln}"])

    prod = random.choice(products)
    cat, base = catalog[prod]
    # price wobble +/- 10%
    price = int(base * random.uniform(0.9, 1.1) / 10) * 10
    qty = random.choices([1, 2, 3, 4, 5], weights=[40, 30, 15, 10, 5])[0]

    county = random.choice(counties_clean)
    # rating loosely higher for cheaper-per-item & electronics, with noise
    rating = random.choices([1, 2, 3, 4, 5], weights=[5, 10, 20, 35, 30])[0]

    row = {
        "order_id": f"ORD{oid}",
        "order_date": messy_date(2025, random.randint(1, 6), random.randint(1, 28)),
        "customer_name": name,
        "phone": messy_phone(),
        "county": messy_county(county),
        "product": prod,
        "category": messy_category(cat),
        "quantity": qty,
        "unit_price": messy_price(price),
        "payment_method": messy_payment(),
        "rating": rating,
    }
    rows.append(row)
    oid += 1

# inject missing values
for r in random.sample(rows, 15):
    r["rating"] = ""
for r in random.sample(rows, 8):
    r["county"] = ""

# inject exact duplicate rows
for r in random.sample(rows, 12):
    rows.append(dict(r))

random.shuffle(rows)

fields = ["order_id", "order_date", "customer_name", "phone", "county",
          "product", "category", "quantity", "unit_price",
          "payment_method", "rating"]

with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print(f"Wrote {len(rows)} rows to {OUT}")
