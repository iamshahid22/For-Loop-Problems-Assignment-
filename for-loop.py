# For Loop Problems Assignment

# Task 1: Calculate the sum of all numbers in a list
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Task 2: Print each character of a string on a new line
def print_characters(text):
    print("\nCharacters in the string:")
    for ch in text:
        print(ch)


# Task 3: Print only the even numbers from a list
def print_even_numbers(numbers):
    print("\nEven numbers:")
    for num in numbers:
        if num % 2 == 0:
            print(num)


# Task 4: Print the length of each word in a list
def print_word_lengths(words):
    print("\nLength of each word:")
    for word in words:
        print(f"{word} : {len(word)}")


# Task 5: Calculate the average of numbers in a list
def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count


# Main Program
numbers = [10, 20, 30, 40, 50, 60]
text = "Python"
words = ["Apple", "Banana", "Computer", "Code"]

print("Task 1")
print("Sum =", calculate_sum(numbers))

print("\nTask 2")
print_characters(text)

print("\nTask 3")
print_even_numbers(numbers)

print("\nTask 4")
print_word_lengths(words)

print("\nTask 5")
print("Average =", calculate_average(numbers))
