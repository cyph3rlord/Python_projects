print("===SIMPLE CALCULATOR===")

# This is the menu bar
while True:
    menu_bar = ["Add", "Subtract", "Multiply", "Divide"]

    for index, menu in enumerate(menu_bar):
        print(f"{index + 1}. {menu}")

# user enters their choice of operation

    choice = input("Enter your choice (1-4): ")
    
    # choice validation
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice")
        continue

# user enter numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter  second number: "))

    # operation decision making
    if choice == "1":
        result = num1 + num2
        print(f"Result = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"Results = {result}")   
    elif choice == "3":
        result = num1 * num2
        print(f"Results = {result}")   
    elif choice == "4":
        if num2 == 0:
            print("Error! cannot divide by zero")  
        else:
            result = num1 / num2
            print(f"Results = {round(result, 2)}")       
    else:
        print("Invalid choice")  
    
    #continuity validation
    try_again = input("Do you wish to continue (Y/N): ")    
    if try_again.lower() == "n":
        break
     
            