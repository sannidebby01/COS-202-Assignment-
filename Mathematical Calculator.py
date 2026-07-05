print("Mathematical Calculator")
while True:
    print("\nMenu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Modulus")
    print("7. Clear")
    print("8. Off")
    
    
    choice = input("Enter your choice: ")
    if choice == "7":
        print("\n" *50)
        print("Calculator Cleared!!")
        continue 
        
    if choice =="8":
        print("Calculator is OFF")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        answer = num1 + num2
        print("Answer =", answer)

    elif choice == "2":
        answer = num1 - num2
        print("Answer =", answer)

    elif choice == "3":
        answer = num1 * num2
        print("Answer =", answer)

    elif choice == "4":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            answer = num1 / num2
            print("Answer =", answer)

    elif choice == "5":
        answer = num1 ** num2
        print("Answer =", answer)

    elif choice == "6":
        answer = num1 % num2
        print("Answer =", answer)

    else:
        print("Invalid choice. Try again.")