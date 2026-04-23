### Academic Data Drift Analyzer
##Overview

This project analyzes how shallow and deep copy affect student data. It generates random academic records, applies mutations, and detects data drift using statistical methods.

 Features
Random student data generation
Shallow vs Deep copy comparison
Data mutation using sqrt()
Statistical analysis (NumPy, Pandas)
Drift detection & classification
# Key Concept
Shallow Copy → modifies original data (shared references)
Deep Copy → safe, independent copy
#Output
Original, Shallow, Deep DataFrames
Drift value
Tuple → (mean, drift, std_dev)
Final classification:
Stable Data
Minor Drift
Critical Drift
Copy Failure
