while True:
    import math 
    #input first_number
    while True:
        try:
            first_num = float(input("enter first_number: "))
        except ValueError:
                print ("Oops! You didn't enter a number. Try again.")
                continue
        else:
            break 
    #input operation     
    while True:              
        operation = (input("enter the operation: "))
        if operation in ["+","-","*","/"]:
            break
        else:
            print("Oops! You didn't enter a operation (+,-,*,/). Try again.")
            continue
    #input sencond_number        
    while True:
            try:
                second_num = float(input("Enter the second_number: "))
                
                if operation == "/" and second_num==0 :

                    raise ZeroDivisionError()
                else:
                     break
            except ValueError:
                print("Invalid input, please enter a numeric value!")
                    
            except ZeroDivisionError:   
                print("Cannot devide by zero ")
           
                
#calculate result
    if operation == "+":
        print(first_num + second_num)
    elif operation =="-": 
        print(first_num - second_num)
    elif operation == "*":
        print(first_num * second_num)
    elif operation == "/":
        print(first_num / second_num)

    else:
        print("invalid input, please enter  numeric value")      

    repeat = input("do you want to perform another operation y/n: " )
    if repeat == "y":
        continue
    elif repeat == "n":
         print("good bye, thanks for your use my calculator")
         break
    else:
        while True:
             repeat = input("do you want to perform another operation y/n: " )             

             