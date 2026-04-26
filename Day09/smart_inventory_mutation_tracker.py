import copy

# Function 1: Create Inventory
def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {"price": 50000, "stock": 10, "supplier": {"rating": 4.5}}
        },
        {
            "item": "Phone",
            "details": {"price": 20000, "stock": 25, "supplier": {"rating": 4.2}}
        }
    ]


# Function 2: Apply Discount & Mutation
def apply_discount(data, roll_no):
    index = roll_no % len(data)

    for i in range(len(data)):
        if i == index:
            # Reduce price by 10%
            data[i]["details"]["price"] *= 0.9
            # Modify stock
            data[i]["details"]["stock"] -= 2


# Function 3: Compare Data
def compare_data(original, modified):
    changed = 0
    unchanged = 0

    for i in range(len(original)):
        if original[i] != modified[i]:
            changed += 1
        else:
            unchanged += 1

    return (changed, unchanged)


# MAIN EXECUTION
roll_no = 576

original_inventory = create_inventory()

# Shallow Copy
shallow_copy = original_inventory.copy()

# Deep Copy
deep_copy = copy.deepcopy(original_inventory)

# Apply mutation
apply_discount(shallow_copy, roll_no)
apply_discount(deep_copy, roll_no)

# Compare results
shallow_result = compare_data(original_inventory, shallow_copy)
deep_result = compare_data(original_inventory, deep_copy)

# OUTPUT
print("Original Inventory:")
print(original_inventory)

print("\nShallow Copy:")
print(shallow_copy)

print("\nDeep Copy:")
print(deep_copy)

print("\nShallow Copy Comparison (changed, unchanged):", shallow_result)
print("Deep Copy Comparison (changed, unchanged):", deep_result)
