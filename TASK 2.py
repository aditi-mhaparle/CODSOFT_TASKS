def calculator():
    print("\n 1.Addition")
    print("\n 2.Substraction")
    print("\n 3.Division")
    print("\n 4.Multiplication")
    choice = input("Enter your choice: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result: ", num1 + num2)

    elif choice == "2":
        print("Result: ", num1 - num2)
    elif choice == "3":
        if num2 != 0:
            print("Result: ", num1 / num2)
        else:
            print("Invalid Second Number!")
    elif choice == "4":
        print("Result: ", num1 * num2)
    else:
        print("Invalid Choice!")

calculator()
