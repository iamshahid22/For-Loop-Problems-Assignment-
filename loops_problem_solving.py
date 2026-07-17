# Loops Problem-Solving Assignment - Student Solution

# Task 1: Countdown Timer
def countdown_timer():
    print("=== Countdown Timer ===")
    for i in range(10, 0, -1):
        print(i)
    print("Boom!")


# Task 2: Find Lucky Number (divisible by 7)
def find_lucky_number():
    print("\n=== Lucky Number (divisible by 7) ===")
    for i in range(1, 51):
        if i % 7 == 0:
            print(f"Lucky Number: {i}")
            break


# Task 3: Game Score Total
def game_score_total():
    scores = [50, 65, 70]
    total = 0
    for score in scores:
        total += score
    print("\n=== Game Score Total ===")
    print("Total Score:", total)


# Task 4: Multiplication Table of 5
def multiplication_table():
    print("\n=== Multiplication Table of 5 ===")
    for i in range(1, 11):
        print(f"5 x {i} = {5 * i}")


# Task 5: Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    print("\n=== Vowel Count ===")
    print(f"String: {s}")
    print("Number of vowels:", count)


# Task 6: Swap Two Numbers (without temp variable)
def swap_numbers(a, b):
    print("\n=== Swap Numbers ===")
    print(f"Before swap: a={a}, b={b}")
    a, b = b, a
    print(f"After swap: a={a}, b={b}")


# Task 7: ATM Withdrawal Simulation
def atm_withdrawal():
    balance = 1000
    amounts = [100, 200, 150]
    print("\n=== ATM Withdrawal Simulation ===")
    print("Initial Balance:", balance)
    for amt in amounts:
        if amt <= balance:
            balance -= amt
            print(f"Withdrew ₹{amt}. Remaining: ₹{balance}")
        else:
            print(f"Cannot withdraw ₹{amt} - Insufficient balance")
    print("Final Balance:", balance)


# Task 8: Highest Marks
def highest_marks():
    marks = [45, 78, 89, 66]
    highest = marks[0]
    for m in marks:
        if m > highest:
            highest = m
    print("\n=== Highest Marks ===")
    print("Marks:", marks)
    print("Highest:", highest)


# Task 9: Number Guess Check (1 to 50)
def number_guess_check(target=25):
    print("\n=== Number Guess Check ===")
    for i in range(1, 51):
        if i == target:
            print(f"Found the number {target} at position {i}")
            break


# Task 10: Count Even Numbers 1-10
def count_even_numbers():
    count = 0
    for i in range(1, 11):
        if i % 2 == 0:
            count += 1
    print("\n=== Even Numbers Count ===")
    print("Even numbers between 1 to 10:", count)


# Task 11: Reverse String using for loop
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    print("\n=== Reverse String ===")
    print(f"Original: {s}")
    print(f"Reversed: {reversed_s}")


# Task 12: Shopping Cart Total
def shopping_cart_total():
    prices = [100, 250, 75]
    total = 0
    for price in prices:
        total += price
    print("\n=== Shopping Cart Total ===")
    print("Total Amount:", total)


# Task 13: Rocket Launch Countdown
def rocket_countdown():
    print("\n=== Rocket Launch Countdown ===")
    for i in range(20, 0, -1):
        print(i)
    print("Launch Successful!")


# Task 14: Count Uppercase Letters
def count_uppercase(s):
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    print("\n=== Uppercase Count ===")
    print(f"String: {s}")
    print("Uppercase letters:", count)


# Task 15: String Length without len()
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    print("\n=== String Length (manual) ===")
    print(f"String: {s}")
    print("Length:", count)


# Task 16: Check Palindrome
def check_palindrome(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    is_pal = s == reversed_s
    print("\n=== Palindrome Check ===")
    print(f"String: {s}")
    print("Is Palindrome:", is_pal)


# Task 17: Second Largest Number
def second_largest():
    nums = [10, 45, 23, 89, 67]
    first = second = float('-inf')
    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n
    print("\n=== Second Largest ===")
    print("Numbers:", nums)
    print("Second Largest:", second)


# Task 18: Simple Interest Calculator
def simple_interest():
    principal = 1000
    rate = 5
    time = 5
    print("\n=== Simple Interest per Year ===")
    for year in range(1, time + 1):
        interest = (principal * rate * year) / 100
        print(f"Year {year}: Interest = ₹{interest:.2f}")


# Task 19: Sum of Odd Numbers 1 to 50
def sum_odd_numbers():
    total = 0
    for i in range(1, 51, 2):
        total += i
    print("\n=== Sum of Odd Numbers (1-50) ===")
    print("Total:", total)


# Task 20: Apply 10% Discount
def apply_discount():
    prices = [500, 1000, 1500]
    print("\n=== Discounted Prices ===")
    for price in prices:
        discounted = price * 0.9
        print(f"Original: ₹{price} → Discounted: ₹{discounted:.2f}")


# Task 21: Perfect Number
def is_perfect_number(num):
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    return sum_div == num

# Test
print("\n=== Perfect Number Check ===")
print("6 is Perfect:", is_perfect_number(6))
print("28 is Perfect:", is_perfect_number(28))


# Task 22: Automorphic Number (example: 25, 76)
def is_automorphic(num):
    sq = num * num
    return str(sq).endswith(str(num))

print("\n=== Automorphic Number ===")
print("25 is Automorphic:", is_automorphic(25))
print("76 is Automorphic:", is_automorphic(76))


# Task 23: Fibonacci Series
def fibonacci_series(n=10):
    print("\n=== Fibonacci Series ===")
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# Task 24: Harshad Number
def is_harshad_number(num):
    digit_sum = 0
    temp = num
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    return num % digit_sum == 0

print("\n=== Harshad Number ===")
print("18 is Harshad:", is_harshad_number(18))
print("42 is Harshad:", is_harshad_number(42))


# Run all tasks
if __name__ == "__main__":
    countdown_timer()
    find_lucky_number()
    game_score_total()
    multiplication_table()
    count_vowels("education")
    swap_numbers(10, 20)
    atm_withdrawal()
    highest_marks()
    number_guess_check()
    count_even_numbers()
    reverse_string("python")
    shopping_cart_total()
    rocket_countdown()
    count_uppercase("PyThOnPrOgRaM")
    string_length("programming")
    check_palindrome("madam")
    second_largest()
    simple_interest()
    sum_odd_numbers()
    apply_discount()
    fibonacci_series()
