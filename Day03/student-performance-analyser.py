# Student Performance Analyzer

name = input("Enter your name: ")

n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    mark = int(input("Enter mark: "))
    marks.append(mark)

valid_count = 0
fail_count = 0

print("\n--- Student Performance ---")

for mark in marks:

    original_mark = mark

    # Personalization:
    # If name length is even, add 1 grace mark (only if mark is valid):
    if len(name) % 2 == 0 and mark >= 0 and mark <= 100:
        mark = mark + 1
        if mark > 100:
            mark = 100

    # Classification:
    if mark < 0 or mark > 100:
        category = "Invalid"

    elif mark >= 90:
        category = "Excellent"
        valid_count = valid_count + 1

    elif mark >= 75:
        category = "Very Good"
        valid_count = valid_count + 1

    elif mark >= 60:
        category = "Good"
        valid_count = valid_count + 1

    elif mark >= 40:
        category = "Average"
        valid_count = valid_count + 1

    else:
        category = "Fail"
        valid_count = valid_count + 1
        fail_count = fail_count + 1

    print(str(original_mark) + " → " + category)

print("Total Valid Students:", valid_count)
print("Total Failed Students:", fail_count)
