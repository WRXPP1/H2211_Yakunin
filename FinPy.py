import requests

idr = input("Vvedit' id - ")

Accessory_type = {
    8: "Hat",
    41: "Hair",
    42: "Face",
    43: "Neck",
    44: "Shoulder",
    45: "Front",
    46: "Back",
    47: "Waist",
}

ssilka = f"https://users.roblox.com/v1/users/{idr}"
res = requests.get(ssilka)

if res.status_code != 200:
    print("Ne znayshov po takomu id")

user = res.json()

print(f"\nUser: {user['name']}")
print(f"Display: {user['displayName']}\n")

lister = []

for accessory_type_id, category_name in Accessory_type.items():
    cursor = None

    while True:
        ssilka = f"https://inventory.roblox.com/v2/users/{idr}/inventory/{accessory_type_id}?limit=100"
        if cursor:
            ssilka += f"&cursor={cursor}"

        res2 = requests.get(ssilka)
        if res2.status_code != 200:
            break

        resour = res2.json()

        for item in resour.get("data", []):
            name = item.get("name") or item.get("assetName") or "Unknown"
            lister.append((category_name, name))

        cursor = resour.get("nextPageCursor")
        if not cursor:
            break

if not lister:
    print("Inventar zhovaniy")
else:
    classc = {}

    for type2, name in lister:
        classc.setdefault(type2, []).append(name)

    for type2, items in classc.items():
        print(f"\n=== {type2} ===")

        index = 1
        for name in items:
            print(f"{index}. {name}")
            index += 1

        print(f"Vs'ogo: {index - 1}")