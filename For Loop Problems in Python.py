# -------------------------------
# Task 1: Print each number and its square
# -------------------------------
print("Task 1: Number and its Square")

numbers = [2, 4, 6, 8, 10]

for num in numbers:
    print(f"{num} -> {num ** 2}")

print("\n" + "-" * 40)

# -------------------------------
# Task 2: Print each character with its index
# -------------------------------
print("Task 2: Characters with Index")

def print_characters(text):
    for index, char in enumerate(text):
        print(f"Index {index}: {char}")

print_characters("Python")

print("\n" + "-" * 40)

# -------------------------------
# Task 3: Sum of even numbers
# -------------------------------
print("Task 3: Sum of Even Numbers")

numbers = [12, 5, 8, 3, 10, 7]

total = 0

for num in numbers:
    if num % 2 == 0:
        total += num

print("Sum of even numbers =", total)

print("\n" + "-" * 40)

# -------------------------------
# Task 4: Print dictionary key-value pairs
# -------------------------------
print("Task 4: Dictionary Key-Value Pairs")

student = {
    "Name": "Shahid",
    "Age": 21,
    "Branch": "CSE"
}

for key, value in student.items():
    print(f"{key} : {value}")

print("\n" + "-" * 40)

# -------------------------------
# Task 5: Numbers divisible by 3 or 5 (1 to 100)
# -------------------------------
print("Task 5: Numbers Divisible by 3 or 5")

numbers = []

for i in range(1, 101):
    numbers.append(i)

for num in numbers:
    if num % 3 == 0 or num % 5 == 0:
        print(num, end=" ")

print()
