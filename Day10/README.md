# Academic Data Drift & Copy Behavior Analyzer

### Overview

This project analyzes how student data changes when copied and modified. It demonstrates the difference between **shallow copy** and **deep copy**, and detects **data drift** using statistical analysis.

### Problem Statement

* Generate student data using random values
* Store data as nested dictionaries
* Convert data into a Pandas DataFrame
* Apply mutations on copied data
* Perform statistical analysis using NumPy
* Detect data drift and copy behavior issues

### Personalization

* Roll Number: **576**
* Rule Used: `576 % 3 = 0`
* Modified indexes: `0, 3, 6, 9` (indexes divisible by 3)

### Features

* Random student data generation
* Nested data structures (list + dictionary + list)
* Shallow copy and deep copy comparison
* Data mutation using mathematical transformation
* Statistical analysis (mean, median, standard deviation)
* Manual mean calculation (without NumPy)
* Data drift detection
* Final classification system

### Technologies Used

* Python
* NumPy
* Pandas
* math module
* random module
* copy module

### How It Works

1. Generate student data
2. Create shallow and deep copies
3. Apply mutation based on roll number rule
4. Convert data into DataFrames
5. Perform statistical analysis
6. Calculate drift between original and modified data
7. Classify system behavior

### Mutation Logic

* Marks updated using: `marks + sqrt(marks)`
* Scores list modified
* Attendance reduced for selected students

### Drift Detection

* Drift = difference between original mean and modified mean
* Custom threshold used for classification

### Output Summary

* Displays original, shallow copy, and deep copy data
* Shows drift value
* Returns tuple: `(mean, drift, std_dev)`
* Final classification:

  * Stable Data
  * Minor Drift
  * Critical Drift
  * Copy Failure Detected

### Key Observation

* **Shallow copy modifies original data** due to shared references
* **Deep copy keeps data independent** and prevents unintended changes

### Learning Outcome

* Understanding of data drift in datasets
* Difference between shallow and deep copy
* Working with NumPy and Pandas
* Importance of proper data handling in real-world systems



