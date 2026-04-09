# ===============================
# Dictionary in Python
# ===============================

# 1. Create a dictionary with 5 student names and their marks
students = {
    "haris": 100,
    "ali": 90,
    "shuja": 99,
    "khizer": 100,
    "ahmed": 80
}

print("Student Names:")
for name in students.keys():
    print(name)

# ==================================

# Footballer Dictionary
footballer = {
    "cristiano": "best",
    "messi": "best",
    "neymar": "best",
    "bale": "good",
    "benzema": "good"
}

# Display values
print("\nQualities:")
for quality in footballer.values():
    print(quality)

# Display keys
print("\nFootballers:")
for name in footballer.keys():
    print(name)

# Access specific value
print("\nBale:", footballer["bale"])

# Check if key exists
if footballer.get('hazard'):
    print("Hazard exists")
else:
    print("Hazard does not exist")

# Access specific key
print("\nMessi:", footballer['messi'])

# Add new key-value pair
footballer['hazard'] = 'good'
print("\nAfter Adding Hazard:", footballer)

# Update value
footballer['hazard'] = 'best'
print("\nAfter Updating Hazard:", footballer)

# Update using update()
footballer.update({'hazard': 'just ok'})
print("\nUpdated Hazard:", footballer['hazard'])

# Remove a key
del footballer['cristiano']
print("\nAfter Deleting Cristiano:", footballer)

# Loop through keys
print("\nKeys:")
for key in footballer.keys():
    print(key)

# Loop through key-value pairs
print("\nKey-Value Pairs:")
for key, value in footballer.items():
    print(key, value)

# Check another key
if footballer.get('kante'):
    print("Humble")
else:
    print("Kante should be added")

# Add Kante
footballer['kante'] = "too humble"

# Check again
if footballer.get('kante'):
    print("Humble")

print("\nDictionary:", footballer)

# Length
print("\nLength:", len(footballer))

# Keys & Items
print("\nKeys:", footballer.keys())
print("Items:", footballer.items())

# Update multiple values
footballer.update({
    'kane': 'ok',
    'cr7': 'goat',
    'mane': 'good'
})

# Remove using pop()
footballer.pop('benzema', None)

print("\nAfter Updates:", footballer)

# Clear dictionary
footballer.clear()
print("\nAfter Clear:", footballer)

# Recreate dictionary
footballer = {
    'kane': 'ok',
    'cr7': 'goat',
    'mane': 'good'
}

print("\nRecreated Dictionary:", footballer)

# Copy dictionary
newfootballer = footballer.copy()
print("\nCopied Dictionary:", newfootballer)

# setdefault()
footballer.setdefault('golden era', 'all')
print("\nAfter setdefault:", footballer)
