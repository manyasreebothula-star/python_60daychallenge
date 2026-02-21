# Emergency Resource Dispatch Analyzer---------------

# Input:----
requests = [10, 25, 60, -3, 0, 45, 80]

# Personalization:---
full_name = "manyasree"
L = len(full_name.replace(" ", ""))
PLI = L % 3

low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []
no_demand = []

total_valid_requests = 0

for req in requests:
    if req < 0:
        invalid_requests.append(req)
    elif req == 0:
        no_demand.append(req)
    elif 1 <= req <= 20:
        low_demand.append(req)
        total_valid_requests += 1
    elif 21 <= req <= 50:
        moderate_demand.append(req)
        total_valid_requests += 1
    elif req > 50:
        high_demand.append(req)
        total_valid_requests += 1

removed_count = 0

if PLI == 0:
    # Rule A :- Remove Low Demand
    removed_count = len(low_demand)
    low_demand = []
    applied_rule = "Rule A - Removed Low Demand"

elif PLI == 1:
    # Rule B :- Remove High Demand
    removed_count = len(high_demand)
    high_demand = []
    applied_rule = "Rule B - Removed High Demand"

elif PLI == 2:
    # Rule C :- Keep Only Moderate Demand
    removed_count = len(low_demand) + len(high_demand)
    low_demand = []
    high_demand = []
    applied_rule = "Rule C - Only Moderate Demand Kept"

# Final Report print:----
print("Full Name Length (L):", L)
print("PLI Value:", PLI)
print("Applied Rule:", applied_rule)

print("\nTotal Valid Requests:", total_valid_requests)
print("Removed Requests Due to PLI:", removed_count)

print("\nFinal Low Demand List:", low_demand)
print("Final Moderate Demand List:", moderate_demand)
print("Final High Demand List:", high_demand)
print("Invalid Requests:", invalid_requests)
print("No Demand Requests:", no_demand)
