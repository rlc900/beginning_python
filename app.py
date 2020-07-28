# print("Hello World")

# MINI CALCULATOR
#
# num1 = input("Enter a number: ")
# num2 = input("*DJ Khalid voice* Anotha one: ")
# result = float(num1) + float(num2)
#
# print(result)

# MAD LIBS
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
#
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# LISTS

fruits = ['apple', 'kiwi', 'banana']
numbers  =[1,4,67,8,24,53,10]

# fruits.extend(numbers)
# fruits.append()
# fruits.insert(1, "pears")
# print(fruits)

# TUPLES
# coordinates = (4, 5)
# print(coordinates[0])
#
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num1 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(23,6,18))

# building a better calulator

# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op == "/":
#     print(num1 / num2)
# else:
#     print("Invalid operator")

secret_word = "slinky"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input('Enter guess: ')
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")




