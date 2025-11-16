# Exercise Solutions

This document contains solutions to selected exercises from the Python Fundamentals course. Try solving the exercises yourself first before checking these solutions!

---

## Module 01: Variables and Data Types

### Exercise 1: Personal Information

```python
# Create variables for personal information
name = "Alice"
age = 25
height = 165.5
likes_python = True

# Print all information
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} cm")
print(f"Likes Python: {likes_python}")
```

### Exercise 2: Type Checking

```python
# Create a variable with the value 3.14
number = 3.14

# Check its type
print(f"Original value: {number}, Type: {type(number)}")

# Convert to integer
number_int = int(number)
print(f"As integer: {number_int}, Type: {type(number_int)}")

# Convert to string
number_str = str(number_int)
print(f"As string: {number_str}, Type: {type(number_str)}")
```

### Exercise 5: F-Strings Practice

```python
product_name = "Apple"
price = 1.50
quantity = 5
total_price = price * quantity

message = f"I bought {quantity} {product_name}(s) for ${total_price}"
print(message)
```

---

## Module 02: Operators and Expressions

### Exercise 1: BMI Calculator

```python
weight = 70  # kg
height = 1.75  # meters

bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")
```

### Exercise 2: Even or Odd

```python
number = 17

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

### Exercise 3: Age Verification

```python
age = 30

can_vote = age >= 18
can_rent_car = age >= 25
can_get_senior_discount = age >= 65

print(f"Can vote: {can_vote}")
print(f"Can rent car: {can_rent_car}")
print(f"Can get senior discount: {can_get_senior_discount}")
```

### Challenge: Leap Year Checker

```python
year = 2024

is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
print(f"{year} is a leap year: {is_leap}")

# Test with other years
for test_year in [2024, 2100, 2000]:
    is_leap = (test_year % 4 == 0) and (test_year % 100 != 0 or test_year % 400 == 0)
    print(f"{test_year}: {is_leap}")
```

---

## Module 03: Control Flow

### Exercise 1: Temperature Classifier

```python
def classify_temperature(temp):
    if temp < 0:
        return "Freezing"
    elif temp <= 15:
        return "Cold"
    elif temp <= 25:
        return "Comfortable"
    else:
        return "Hot"

# Test with different temperatures
for temp in [-5, 10, 20, 30]:
    print(f"{temp}°C: {classify_temperature(temp)}")
```

### Exercise 2: FizzBuzz

```python
for num in range(1, 31):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
```

### Exercise 3: Factorial Calculator

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"5! = {factorial(5)}")  # 120
```

### Exercise 4: Prime Number Checker

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test
for num in [7, 12, 17, 20]:
    print(f"{num} is prime: {is_prime(num)}")
```

---

## Module 04: Functions

### Exercise 1: Temperature Converter

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test
print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"100°F = {fahrenheit_to_celsius(100):.1f}°C")
```

### Exercise 2: Find Maximum

```python
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Or more concisely:
def find_max_simple(a, b, c):
    return max(a, b, c)

print(find_max(5, 10, 3))  # 10
```

### Exercise 3: Palindrome Checker

```python
def is_palindrome(text):
    # Remove spaces and convert to lowercase
    text = text.replace(" ", "").lower()
    return text == text[::-1]

# Test
words = ["radar", "level", "noon", "python"]
for word in words:
    print(f"{word}: {is_palindrome(word)}")
```

### Exercise 4: Count Vowels

```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Or using list comprehension:
def count_vowels_short(text):
    return sum(1 for char in text if char.lower() in 'aeiou')

print(count_vowels("Hello World"))  # 3
```

---

## Module 05: Data Structures

### Exercise 1: List Statistics

```python
def get_stats(numbers):
    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "avg": sum(numbers) / len(numbers)
    }

numbers = [1, 2, 3, 4, 5]
stats = get_stats(numbers)
print(stats)
```

### Exercise 2: Remove Duplicates

```python
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Or using dict (Python 3.7+)
def remove_duplicates_dict(lst):
    return list(dict.fromkeys(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 3, 5]))  # [1, 2, 3, 4, 5]
```

### Exercise 3: Word Frequency Counter

```python
def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Or using Counter
from collections import Counter
def word_frequency_counter(sentence):
    return dict(Counter(sentence.lower().split()))

print(word_frequency("hello world hello"))
```

---

## Module 06: File Handling

### Exercise 1: Word Counter

```python
def count_file_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            return {
                "lines": len(lines),
                "words": word_count
            }
    except FileNotFoundError:
        return {"error": "File not found"}

print(count_file_words('../data/sample_files/sample.txt'))
```

---

## Module 07: Error Handling

### Exercise 1: Safe Calculator

```python
def safe_calculator(a, b, operator):
    try:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                return "Error: Division by zero"
            return a / b
        else:
            return "Error: Invalid operator"
    except Exception as e:
        return f"Error: {e}"

print(safe_calculator(10, 5, '+'))   # 15
print(safe_calculator(10, 0, '/'))   # Error: Division by zero
```

### Exercise 2: List Element Access

```python
def safe_get(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default

# Test
my_list = [1, 2, 3]
print(safe_get(my_list, 1))     # 2
print(safe_get(my_list, 10))    # None
print(safe_get(my_list, 10, 0)) # 0
```

---

## Module 09: OOP Basics

### Exercise 1: Rectangle Class

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

# Test
rect = Rectangle(5, 3)
print(rect)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
print(f"Is square: {rect.is_square()}")
```

### Exercise 2: Student Class

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100")

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def pass_fail(self):
        avg = self.average_grade()
        return "Pass" if avg >= 60 else "Fail"

# Test
student = Student("Alice")
student.add_grade(85)
student.add_grade(90)
student.add_grade(78)
print(f"Average: {student.average_grade()}")
print(f"Status: {student.pass_fail()}")
```

---

## Tips for Solving Exercises

1. **Read the requirements carefully** - Make sure you understand what's being asked
2. **Start simple** - Get a basic version working first
3. **Test as you go** - Don't wait until the end to test your code
4. **Use print statements** - Debug by printing intermediate values
5. **Refer to module examples** - Look back at similar code
6. **Don't worry about perfection** - Your first solution doesn't need to be perfect
7. **Refactor later** - Once it works, you can improve it
8. **Ask for help** - If stuck, search online or ask in communities

---

## Additional Practice Resources

- [HackerRank Python](https://www.hackerrank.com/domains/python) - Coding challenges
- [LeetCode](https://leetcode.com/) - Algorithm problems
- [Codewars](https://www.codewars.com/) - Kata exercises
- [Exercism Python Track](https://exercism.org/tracks/python) - Mentored exercises
- [Python Koans](https://github.com/gregmalcolm/python_koans) - Learn through testing

Keep practicing and happy coding! 🐍
