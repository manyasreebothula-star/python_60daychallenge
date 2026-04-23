import random
import math
import copy
import numpy as np
import pandas as pd


# Function 1: Generate Data

def generate_students(n=12):
    students = []
    for i in range(n):
        student = {
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        students.append(student)
    return students


# Function 2: Manual Mean (without NumPy)

def manual_mean(data):
    total = sum([s["marks"] for s in data])
    return total / len(data)



# Function 3: Mutate Data

def mutate_data(data, roll_no):
    for i in range(len(data)):
        if i % (roll_no % 3 + 1) == 0:   # rule based on roll number
            data[i]["marks"] += math.sqrt(data[i]["marks"])
            data[i]["attendance"] += 5
            data[i]["scores"][0] += 2   # modifying inner list
    return data



# Function 4: Analyze Data

def analyze_data(original, modified):
    orig_marks = np.array([s["marks"] for s in original])
    mod_marks = np.array([s["marks"] for s in modified])

    mean = np.mean(mod_marks)
    median = np.median(mod_marks)
    std_dev = np.std(mod_marks)

    drift = abs(np.mean(orig_marks) - mean)

    # normalization
    normalized = (mod_marks - np.min(mod_marks)) / (np.max(mod_marks) - np.min(mod_marks))

    return mean, median, std_dev, drift, normalized



# Function 5: Classification

def classify(drift, threshold, original, shallow):
    if original != shallow:
        return "Copy Failure Detected"
    elif drift < threshold:
        return "Stable Data"
    elif drift < threshold * 2:
        return "Minor Drift"
    else:
        return "Critical Drift"


# MAIN PROGRAM

roll_no = 7   # change this to your roll number

# Step 1: Generate Data
original_data = generate_students()

# Step 2: Copies
shallow_copy = copy.copy(original_data)
deep_copy = copy.deepcopy(original_data)

# Step 3: Mutate ONLY copies
mutate_data(shallow_copy, roll_no)
mutate_data(deep_copy, roll_no)

# Step 4: Convert to DataFrame
df_original = pd.DataFrame(original_data)
df_shallow = pd.DataFrame(shallow_copy)
df_deep = pd.DataFrame(deep_copy)

# Step 5: Analysis
mean, median, std_dev, drift, normalized = analyze_data(original_data, deep_copy)

manual_avg = manual_mean(original_data)

# Custom threshold
threshold = 5

# Step 6: Classification
result = classify(drift, threshold, original_data, shallow_copy)

# -----------------------------
# OUTPUT
# -----------------------------
print("\nOriginal Data:\n", df_original)
print("\nShallow Copy:\n", df_shallow)
print("\nDeep Copy:\n", df_deep)

print("\nManual Mean (without NumPy):", manual_avg)
print("\nTuple Output (mean, drift, std_dev):", (mean, drift, std_dev))
print("\nDrift Value:", drift)

print("\nFinal Classification:", result)
