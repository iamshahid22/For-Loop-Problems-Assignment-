# For Loop Problem Solving in Python

# Task 1: Print numbers from 1 to 10 excluding 5
print("Task 1: Numbers from 1 to 10 (excluding 5)")
for i in range(1, 11):
    if i != 5:
        print(i, end=" ")
print("\n")


# Task 2: Print each string in uppercase
print("Task 2: Strings in Uppercase")

def print_uppercase(words):
    for word in words:
        print(word.upper())

names = ["python", "java", "html", "css"]
print_uppercase(names)
print()


# Task 3: Sum of even numbers in a list
print("Task 3: Sum of Even Numbers")
numbers = [10, 15, 20, 25, 30, 35]
total = 0

for num in numbers:
    if num % 2 == 0:
        total += num

print("Sum of Even Numbers =", total)
print()


# Task 4: Print dictionary key-value pairs
print("Task 4: Dictionary Key-Value Pairs")
student = {
    "Name": "Shahid",
    "Age": 21,
    "Course": "B.Tech CSE"
}

for key, value in student.items():
    print(key, ":", value)
print()


# Task 5: Fibonacci Sequence (First 10 Numbers)
print("Task 5: Fibonacci Sequence")
a = 0
b = 1

for i in range(10):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
print("\n")


# Task 6: Average Exam Score
print("Task 6: Average Exam Score")
scores = [75, 80, 90, 85, 70]

total = 0
count = 0

for score in scores:
    total += score
    count += 1

average = total / count
print("Average Score =", average)
print()


# Task 7: Print a 5x5 Matrix (1 to 25)
print("Task 7: 5x5 Matrix")
num = 1

for i in range(5):
    for j in range(5):
        print(num, end="\t")
        num += 1
    print()
