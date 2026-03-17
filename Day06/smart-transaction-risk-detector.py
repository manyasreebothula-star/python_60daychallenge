# Smart Transaction Risk Detector

def analyze_transactions(transactions):
    # Dictionary for classification
    categorized = {
        "normal": [],
        "large": [],
        "high_risk": [],
        "invalid": []
    }

    # Classification using loop + conditions
    for t in transactions:
        if t <= 0:
            categorized["invalid"].append(t)
        elif 1 <= t <= 500:
            categorized["normal"].append(t)
        elif 501 <= t <= 2000:
            categorized["large"].append(t)
        else:
            categorized["high_risk"].append(t)

    # Using list comprehension (only valid transactions)
    valid_transactions = [t for t in transactions if t > 0]

    # Summary using tuple
    total_value = sum(valid_transactions)
    count = len(transactions)
    summary = (total_value, count)

    # Pattern Detection
    frequent = count > 5
    large_spending = total_value > 5000
    suspicious = len(categorized["high_risk"]) >= 3

    # Final Risk Classification
    if suspicious or (frequent and large_spending):
        risk = "High Risk"
    elif frequent or large_spending:
        risk = "Moderate Risk"
    else:
        risk = "Low Risk"

    # Output:---
    print("Categorized Transactions:")
    print(categorized)
    print("\nTotal Transaction Value:", summary[0])
    print("Number of Transactions:", summary[1])
    print("Final Risk Classification:", risk)


# Eg:-
transactions = [200, 1500, 3000, -50, 700, 2500, 100]
analyze_transactions(transactions)
