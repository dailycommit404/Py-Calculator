# Claculator Code
# if op == '+':	Checks if the operator is addition.
# print(a+b)	Adds two numbers and displays the result.
# elif op == '-':	Checks if the operator is subtraction.
# print(a-b)	Subtracts two numbers.
# elif op == '*':	Checks if the operator is multiplication.
# print(a*b)	Multiplies two numbers.
# elif op == '/':	Checks if the operator is division.
# print(a/b)	Divides two numbers.
# elif op == '**':Checks if the operator is exponentiation.
# print(a**b)	Calculates power (a raised to b).
# else:	Executes when no operator matches.
# print("INVALID OPERATOR")	Displays an invalid operator message.

# Remember these operators
# + → Addition
# - → Subtraction
# * → Multiplication
# / → Division
# ** → Power (Exponentiation)
# Important: == means comparison, whereas = means assignment.

# Actual Code

a = float(input("Enter 1 number:"))
b = float(input("Enter 2 number:"))
op =input("Enter operator(+, *, /, m, %, **): ")

if op == '+':
    print(a+b)

elif op == '-':
    print(a-b)

elif op == '*':
    print(a*b)

elif op == '/':
    print(a/b)

elif op == '**':
    print(a**b)

else:
    print("INVALID OPERATOR")
