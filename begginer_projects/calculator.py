import math

print("WELCOME TO MY MINI CALCULATOR\n")

#taking input
try:
    first_num = float(input("Enter the first number\n"))
    sec_num = float(input("Enter the second number\n"))

    print("\nchoose an option")

    print("1 - add")
    print("2 - subtract")
    print("3 - divide")
    print("4 - multiply")
    print("5 - maximum")
    print("6 - minimum")
    print("7 - square root of first number")
    print("8 - round second number")


    choice = input("\nchoose from 1-8 to perform a calculation\n")
    if choice == "1":
        print("Result: ", first_num + sec_num)
    
    elif choice == "2":
        print("Result: ", first_num - sec_num)

    elif choice == "3":
        try:
             print("Result: ", round(first_num / sec_num, 2))
        except ZeroDivisionError:
            print(" Can't divide by zero")
    
    elif choice == "4":
         print("Result: ", first_num * sec_num) 

    elif choice == "5":
        print("Maximum value: ", max(first_num,  sec_num))

    elif choice == "6":
        print("minimum value: ", min(first_num, sec_num))
    
    elif choice == "7":
         if first_num <0:
             print(" Can't find the square root of a negative number")
        
         else:
             print("Square root: ", math.sqrt(first_num) )   
         
    elif choice == "8":
         print("Rounded number: ", round(sec_num))  
         
    else:
        print(" Invalid choice choose between 1 - 8") 
except ValueError:
         print("Enter a valid number")  
                                               



