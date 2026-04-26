import random
import copy
import math
import numpy as np
import pandas as pd

# Function 1: Generate Data
def generate_data():
    data = []
    for i in range(10):
        student = {
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        data.append(student)
    return data


# Function 2: Apply Mutation
def apply_mutation(data, roll_no):
    rule = roll_no % 3  # 576 % 3 = 0

    for i in range(len(data)):
        if i % 3 == rule:
            # Modify marks
            data[i]["marks"] += math.sqrt(data[i]["marks"])
            
            # Modify scores (nested list)
            data[i]["scores"][0] += 5
            
            # Modify attendance
            data[i]["attendance"] -= 5


# Function 3: Analysis
def analyze(data):
    marks = [d["marks"] for d in data]
    
    mean = np.mean(marks)
    median = np.median(marks)
    std = np.std(marks)

    return mean, median, std


# Function 4: Manual Mean (without NumPy)
def manual_mean(data):
    total = 0
    for d in data:
        total += d["marks"]
    return total / len(data)


# Function 5: Drift Detection
def detect_drift(original, modified):
    orig_mean = manual_mean(original)
    mod_mean = manual_mean(modified)

    drift = abs(orig_mean - mod_mean)
    return drift, orig_mean


# MAIN
roll_no = 576

original = generate_data()

# Copies
shallow_copy = original.copy()
deep_copy = copy.deepcopy(original)

# Apply mutation
apply_mutation(shallow_copy, roll_no)
apply_mutation(deep_copy, roll_no)

# Convert to DataFrame
df_original = pd.DataFrame(original)
df_shallow = pd.DataFrame(shallow_copy)
df_deep = pd.DataFrame(deep_copy)

# Analysis
mean, median, std = analyze(deep_copy)

# Drift
drift, original_mean = detect_drift(original, deep_copy)

# Custom threshold
threshold = 5

# Classification
if original != shallow_copy:
    copy_status = "Copy Failure Detected"
elif drift > threshold:
    copy_status = "Critical Drift"
elif drift > 2:
    copy_status = "Minor Drift"
else:
    copy_status = "Stable Data"

# OUTPUT
print("Original DataFrame:\n", df_original)
print("\nShallow Copy:\n", df_shallow)
print("\nDeep Copy:\n", df_deep)

print("\nDrift Value:", drift)
print("Tuple (mean, drift, std):", (mean, drift, std))

print("\nFinal Classification:", copy_status)
