#01 positive negative zero.py
# num = float(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

#02 even odd.py
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#03 greatest of two.py
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# if a > b:
#     print("Greatest:", a)
# elif b > a:
#     print("Greatest:", b)
# else:
#     print("Both numbers are equal")

#04 greatest of three.py
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Greatest:", a)
# elif b >= a and b >= c:
#     print("Greatest:", b)
# else:
#     print("Greatest:", c)

#05 voting eligibility.py
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

#06 leap year.py
# year = int(input("Enter a year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

#07 vowel or consonant.py
# char = input("Enter a character: ").lower()

# if char in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")

#08 divisible by 5 and 11.py
# num = int(input("Enter a number: "))

# if num % 5 == 0 and num % 11 == 0:
#     print("The number is divisible by both 5 and 11.")
# else:
#     print("The number is not divisible by both 5 and 11.")

#09 divisible by 3 or 7.py
# num = int(input("Enter a number: "))

# if num % 3 == 0 or num % 7 == 0:
#     print("The number is divisible by 3 or 7.")
# else:
#     print("The number is not divisible by 3 or 7.")

#10 grades based on marks.py
# marks = float(input("Enter marks: "))

# if 90 <= marks <= 100:
#     grade = "A"
# elif 80 <= marks <= 89:
#     grade = "B"
# elif 70 <= marks <= 79:
#     grade = "C"
# elif 60 <= marks <= 69:
#     grade = "D"
# elif 0 <= marks < 60:
#     grade = "F"
# else:
#     grade = "Invalid marks"

# print("Grade:", grade)

#11 uppercase or lowercase.py
# char = input("Enter a character: ")

# if char.isupper():
#     print("Uppercase")
# elif char.islower():
#     print("Lowercase")
# else:
#     print("It is not an alphabetic character.")

#12 vowel using elif.py
# char = input("Enter a character: ").lower()

# if char == "a":
#     print("Vowel")
# elif char == "e":
#     print("Vowel")
# elif char == "i":
#     print("Vowel")
# elif char == "o":
#     print("Vowel")
# elif char == "u":
#     print("Vowel")
# else:
#     print("Consonant")

#13 check three sides form triangle.py
# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:
#     print("The three sides can form a triangle.")
# else:
#     print("The three sides cannot form a triangle.")

#14 triangle type.py
# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# if a + b <= c or a + c <= b or b + c <= a:
#     print("Invalid triangle")
# elif a == b == c:
#     print("Equilateral triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")

#15 largest of four.py
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))
# d = float(input("Enter fourth number: "))

# largest = a

# if b > largest:
#     largest = b
# if c > largest:
#     largest = c
# if d > largest:
#     largest = d

# print("Largest:", largest)

#16 three digit number.py
# num = int(input("Enter a number: "))

# if 100 <= abs(num) <= 999:
#     print("It is a three-digit number.")
# else:
#     print("It is not a three-digit number.")

#17 electricity bill.py
# units = float(input("Enter electricity units: "))

# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = 100 * 5 + (units - 100) * 7
# else:
#     bill = 100 * 5 + 100 * 7 + (units - 200) * 10

# print("Electricity bill: ₹", bill)

#18 tax based on income.py
# income = float(input("Enter annual income: "))

# if income <= 250000:
#     tax = 0
# elif income <= 500000:
#     tax = (income - 250000) * 0.05
# elif income <= 1000000:
#     tax = 12500 + (income - 500000) * 0.20
# else:
#     tax = 112500 + (income - 1000000) * 0.30

# print("Tax amount: ₹", tax)

#19 student pass fail.py
# marks1 = float(input("Enter marks for Subject 1: "))
# marks2 = float(input("Enter marks for Subject 2: "))
# marks3 = float(input("Enter marks for Subject 3: "))

# if marks1 >= 35 and marks2 >= 35 and marks3 >= 35:
#     print("Student Passed")
# else:
#     print("Student Failed")

#20 minimum three subjects.py
# marks1 = float(input("Enter marks for Subject 1: "))
# marks2 = float(input("Enter marks for Subject 2: "))
# marks3 = float(input("Enter marks for Subject 3: "))

# minimum = min(marks1, marks2, marks3)

# if minimum >= 35:
#     print("Student Passed")
# else:
#     print("Student Failed")

#21 simple calculator.py
# a = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# b = float(input("Enter second number: "))

# if operator == "+":
#     print("Result:", a + b)
# elif operator == "-":
#     print("Result:", a - b)
# elif operator == "*":
#     print("Result:", a * b)
# elif operator == "/":
#     if b != 0:
#         print("Result:", a / b)
#     else:
#         print("Cannot divide by zero.")
# else:
#     print("Invalid operator.")

#22 century year.py
# year = int(input("Enter a year: "))

# if year % 100 == 0:
#     print("It is a century year.")
# else:
#     print("It is not a century year.")

#23 days in month.py
# month = int(input("Enter month number (1-12): "))

# if month in [1, 3, 5, 7, 8, 10, 12]:
#     print("31 days")
# elif month in [4, 6, 9, 11]:
#     print("30 days")
# elif month == 2:
#     print("28 or 29 days")
# else:
#     print("Invalid month")

#24 days in month input.py
# month = int(input("Enter month number (1-12): "))
# year = int(input("Enter year: "))

# if month == 2:
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         days = 29
#     else:
#         days = 28
# elif month in [4, 6, 9, 11]:
#     days = 30
# elif month in [1, 3, 5, 7, 8, 10, 12]:
#     days = 31
# else:
#     days = 0

# if days:
#     print("Number of days:", days)
# else:
#     print("Invalid month")

#25 password validation.py
# password = input("Enter password: ")

# if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
#     print("Password is valid.")
# else:
#     print("Password is invalid.")
# print("Password must contain at least 8 characters, including letters and digits.")

#26 multiple conditions.py
# length = int(input("Enter password length: "))
# has_digit = input("Does it contain a digit? (yes/no): ").lower()
# has_special = input("Does it contain a special character? (yes/no): ").lower()

# if length >= 8 and has_digit == "yes" and has_special == "yes":
#     print("Password meets all conditions.")
# else:
#     print("Password does not meet all conditions.")

#27 discount based on purchase.py
# amount = float(input("Enter purchase amount: "))

# if amount >= 5000:
#     discount = amount * 0.20
# elif amount >= 3000:
#     discount = amount * 0.15
# elif amount >= 1000:
#     discount = amount * 0.10
# else:
#     discount = 0

# final_amount = amount - discount

# print("Discount: ₹", discount)
# print("Final amount: ₹", final_amount)

#28 driving license.py
# age = int(input("Enter your age: "))
# has_learner_license = input("Do you have a learner license? (yes/no): ").lower()

# if age >= 18 and has_learner_license == "yes":
#     print("Eligible for driving license.")
# else:
#     print("Not eligible for driving license.")

#29 login system.py
# correct_username = "admin"
# correct_password = "1234"

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == correct_username and password == correct_password:
#     print("Login successful.")
# else:
#     print("Invalid username or password.")

#30 menu driven calculator.py
# while True:
#     print("\n--- Calculator Menu ---")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "5":
#         print("Exiting calculator...")
#         break

#     if choice in ["1", "2", "3", "4"]:
#         a = float(input("Enter first number: "))
#         b = float(input("Enter second number: "))

#         if choice == "1":
#             print("Result:", a + b)
#         elif choice == "2":
#             print("Result:", a - b)
#         elif choice == "3":
#             print("Result:", a * b)
#         elif choice == "4":
#             if b != 0:
#                 print("Result:", a / b)
#             else:
#                 print("Cannot divide by zero.")
#     else:
#         print("Invalid choice.")
