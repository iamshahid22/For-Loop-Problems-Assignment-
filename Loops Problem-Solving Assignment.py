# Loops Problem-Solving Assignment

# 1. Countdown Timer
print("1. Countdown Timer")
for i in range(10, 0, -1):
    print(i)
print("Boom!\n")

# 2. Find Lucky Numbers (Divisible by 7)
print("2. Lucky Numbers (Divisible by 7)")
for i in range(1, 51):
    if i % 7 == 0:
        print(i, end=" ")
print("\n")

# 3. Game Score Total
print("3. Game Score Total")
scores = [50, 65, 70]
total = 0
for score in scores:
    total += score
print("Total Score =", total)
print()

# 4. Multiplication Table of 5
print("4. Multiplication Table of 5")
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")
print()

# 5. Count Vowels
print("5. Count Vowels")
text = "Programming"
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Vowels =", count)
print()

# 6. Swap Two Numbers
print("6. Swap Two Numbers")
a = 10
b = 20
print("Before:", a, b)
a = a + b
b = a - b
a = a - b
print("After :", a, b)
print()

# 7. ATM Withdrawal
print("7. ATM Withdrawal")
balance = 1000
withdrawals = [100, 200, 150]
for amount in withdrawals:
    balance -= amount
    print("Withdraw:", amount, "Balance:", balance)
print()

# 8. Highest Marks
print("8. Highest Marks")
marks = [45, 78, 89, 66]
highest = marks[0]
for mark in marks:
    if mark > highest:
        highest = mark
print("Highest Marks =", highest)
print()

# 9. Number Guess Check
print("9. Number Guess Check")
guess = 25
for i in range(1, 51):
    if i == guess:
        print("Number Found:", i)
        break
print()

# 10. Count Even Numbers
print("10. Count Even Numbers")
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += 1
print("Even Numbers =", count)
print()

# 11. Reverse String
print("11. Reverse String")
text = "python"
reverse = ""
for i in range(len(text)-1, -1, -1):
    reverse += text[i]
print("Reverse =", reverse)
print()

# 12. Shopping Cart Total
print("12. Shopping Cart Total")
prices = [100, 250, 75]
total = 0
for price in prices:
    total += price
print("Total =", total)
print()

# 13. Rocket Launch Countdown
print("13. Rocket Launch Countdown")
for i in range(20, 0, -1):
    print(i)
print("Launch Successful!\n")

# 14. Count Uppercase Letters
print("14. Count Uppercase Letters")
text = "PyThOnPrOgRaM"
count = 0
for ch in text:
    if ch.isupper():
        count += 1
print("Uppercase Letters =", count)
print()

# 15. String Length Without len()
print("15. String Length Without len()")
text = "programming"
length = 0
for ch in text:
    length += 1
print("Length =", length)
print()

# 16. Palindrome Check
print("16. Palindrome Check")
text = "madam"
reverse = ""
for i in range(len(text)-1, -1, -1):
    reverse += text[i]
if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
print()

# 17. Second Largest Number
print("17. Second Largest Number")
numbers = [10, 45, 23, 89, 67]
largest = second = -999999
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second Largest =", second)
print()

# 18. Simple Interest
print("18. Simple Interest")
principal = 1000
rate = 5
for year in range(1, 6):
    interest = (principal * rate * year) / 100
    print("Year", year, "Interest =", interest)
print()

# 19. Sum of Odd Numbers
print("19. Sum of Odd Numbers")
total = 0
for i in range(1, 51):
    if i % 2 != 0:
        total += i
print("Sum =", total)
print()

# 20. Apply 10% Discount
print("20. Discounted Prices")
prices = [500, 1000, 1500]
for price in prices:
    new_price = price - (price * 10 / 100)
    print(new_price)
print()

# 21. Perfect Number
print("21. Perfect Number")
num = 28
sum_div = 0
for i in range(1, num):
    if num % i == 0:
        sum_div += i
if sum_div == num:
    print(num, "is Perfect Number")
else:
    print(num, "is Not Perfect Number")
print()

# 22. Automorphic Number
print("22. Automorphic Number")
num = 25
square = num * num
if str(square).endswith(str(num)):
    print(num, "is Automorphic")
else:
    print(num, "is Not Automorphic")
print()

# 23. Fibonacci Series
print("23. Fibonacci Series")
a = 0
b = 1
for i in range(10):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
print("\n")

# 24. Harshad Number
print("24. Harshad Number")
num = 18
digit_sum = 0
temp = num
while temp > 0:
    digit_sum += temp % 10
    temp //= 10

if num % digit_sum == 0:
    print(num, "is Harshad Number")
else:
    print(num, "is Not Harshad Number")
