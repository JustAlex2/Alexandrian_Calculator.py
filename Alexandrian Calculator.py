while True:
    print("\nDescription\n")
    print("The Alexandrian Calculator is a program supposed to operate different calculations ranging from division to comparasion")
    print("It's my first project and because of that the code is not very sophisticated however it is open-source.")
    print("It may be upgraded with new features as time passes.For the newest version contact the developer")
    print("Current version: 1.1")
    print("\nOptions\n")
    print("Enter 'add' to add two numbers")
    print("Enter 'substract' to substract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("In order to find out if the first number is bigger than the second enter the command 'bigger' ")
    print("If you want to see if the first number is smaller than the second enter the command 'smaller' ")
    print("If you want to see if a the first number is bigger or equal than the second enter 'be' ")
    print("If you want to see if the first number is smaller or equal than the second enter 'se' ")
    user_input = input(": ")
    if user_input == "quit":
        break
    if user_input == "add":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 + num2)
        print("\nThe answer is " + result)

    elif user_input == "substract":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 - num2)
        print("\nThe answer is " + result)

    elif user_input == "multiply":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 * num2)
        print("\nThe answer is " + result)

    elif user_input == "divide":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 / num2)
        print("\nThe answer is " + result)
    if user_input == "bigger":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 > num2)
        print("\nThe answer is " + result)

    elif user_input == "smaller":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 < num2)
        print("\nThe answer is " + result)

    elif user_input == "be":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 >= num2)
        print("\nThe answer is " + result)

    elif user_input == "se":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 <= num2)
        print("\nThe answer is " + result)

    else:
        print("Unknown input")