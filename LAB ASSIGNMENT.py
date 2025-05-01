#Ayesha Asghar
#SP24-BBA-015
#LAB ASSIGNMENT

# Dictionary: Pakistani fruits with their prices per kg (in PKR)
fruit_prices = {
    "Mango": 180,
    "Banana": 100,
    "Apple": 250,
    "Orange": 150,
    "Grapes": 220,
    "Guava": 90,
    "Pomegranate": 300,
    "Peach": 160,
    "Papaya": 140,
    "Watermelon": 60
}

# 1. get() – Retrieve price of a fruit
print("1. Price of Mango:", fruit_prices.get("Mango"))

# 2. keys() – Show all fruits
print("2. Available fruits:", list(fruit_prices.keys()))

# 3. values() – Show all prices
print("3. Fruit prices:", list(fruit_prices.values()))

# 4. items() – Get all fruit-price pairs
print("4. Full price list:", list(fruit_prices.items()))

# 5. update() – Add a new fruit or change price
fruit_prices.update({"Strawberry": 270})
print("5. After adding Strawberry:", fruit_prices)

# 6. pop() – Remove a fruit by name
removed_price = fruit_prices.pop("Guava")
print("6. Removed Guava (was PKR", removed_price, "per kg)")

# 7. popitem() – Remove the last inserted item
last_item = fruit_prices.popitem()
print("7. Last item removed:", last_item)

# 8. setdefault() – Add a fruit if it doesn't exist
fruit_prices.setdefault("Cherry", 320)
print("8. After setdefault for Cherry:", fruit_prices)

# 9. copy() – Create a backup of the fruit_prices
backup_prices = fruit_prices.copy()
print("9. Backup copy:", backup_prices)

# 10. clear() – Clear the backup dictionary
backup_prices.clear()
print("10. Cleared backup:", backup_prices)