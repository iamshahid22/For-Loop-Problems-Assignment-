# For Loop Problems in Python - Student Solution

# Task 1: Print number and its square
def print_numbers_and_squares():
    """Iterate over a list and print number with its square."""
    numbers = [2, 5, 8, 10, 12, 15]
    print("=== Task 1: Numbers and Their Squares ===")
    for num in numbers:
        print(f"Number: {num} | Square: {num * num}")


# Task 2: Print each character with index
def print_char_with_index(s):
    """Print each character of string with its index using for loop."""
    print(f"\n=== Task 2: Characters with Index (String: '{s}') ===")
    for index in range(len(s)):
        print(f"Index {index}: {s[index]}")


# Task 3: Sum of even numbers in list
def sum_even_numbers(numbers):
    """Calculate sum of all even numbers using for loop."""
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

# Test
print("\n=== Task 3: Sum of Even Numbers ===")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List: {nums}")
print("Sum of even numbers:", sum_even_numbers(nums))


# Task 4: Iterate over dictionary
def print_dictionary(d):
    """Print key-value pairs using for loop."""
    print("\n=== Task 4: Dictionary Key-Value Pairs ===")
    for key, value in d.items():
        print(f"{key} : {value}")

# Test
student = {
    "Name": "Aarav",
    "Age": 19,
    "Course": "Engineering",
    "CGPA": 8.7,
    "City": "Mumbai"
}
print_dictionary(student)


# Task 5: Numbers 1-100 divisible by 3 or 5
def print_divisible_by_3_or_5():
    """Generate numbers 1-100 and print those divisible by 3 or 5."""
    print("\n=== Task 5: Numbers Divisible by 3 or 5 (1 to 100) ===")
    divisible_list = []
    
    # Generate list using for loop
    numbers = []
    for i in range(1, 101):
        numbers.append(i)
    
    # Second loop to filter and print
    for num in numbers:
        if num % 3 == 0 or num % 5 == 0:
            divisible_list.append(num)
            print(num, end=" ")
    
    print("\n\nTotal numbers divisible by 3 or 5:", len(divisible_list))


# ==================== Run All Tasks ====================
if __name__ == "__main__":
    print("=" * 60)
    print("FOR LOOP PROBLEMS - COMPLETE STUDENT SOLUTION")
    print("=" * 60)
    
    print_numbers_and_squares()
    print_char_with_index("Python")
    sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # already printed inside
    print_dictionary({"apple": 10, "banana": 20, "cherry": 30})
    print_divisible_by_3_or_5()
    
    print("\n" + "=" * 60)
    print("All tasks completed successfully!")
    print("=" * 60)
