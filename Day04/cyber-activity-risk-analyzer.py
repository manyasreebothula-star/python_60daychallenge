register_number = 24110011576
D = register_number % 10

print("Register Digit (D):", D)

activity_scores = [10, 45, 78, 120, -5, 30, 99, 150]

low_risk = []
medium_risk = []
high_risk = []
critical_risk = []

valid_count = 0
ignored_count = 0
removed_due_to_personalization = 0

# Categorization
for score in activity_scores:

    if score < 0:
        ignored_count = ignored_count + 1

    else:
        valid_count = valid_count + 1

        if score <= 30:
            low_risk.append(score)

        elif score <= 60:
            medium_risk.append(score)

        elif score <= 100:
            high_risk.append(score)

        else:
            critical_risk.append(score)

print("\nBefore Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

# Personalized Filtering
if D % 2 == 0:
    removed_due_to_personalization = len(low_risk)
    low_risk = []
else:
    removed_due_to_personalization = len(critical_risk)
    critical_risk = []

print("\nAfter Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

print("\nTotal Valid Entries:", valid_count)
print("Ignored Entries:", ignored_count)
print("Removed Due to Personalization:", removed_due_to_personalization)
