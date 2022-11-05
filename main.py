# Program make a simple calculator

from io import StringIO
from main_func import *
from log_func import *
    
def returnPrint(*message):
    io=StringIO()
    print(*message, file=io)
    return io.getvalue()
    
print("Calculator started.")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    
    abnormal=False;

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except:
            print("You can only enter numbers")
            continue ###try 부분으로 다시 돌아갈 수 있게?
        

        if choice == '1':
            operator="+"
            log=returnPrint(num1, operator, num2, "=", add(num1, num2))
            print(log)

        elif choice == '2':
            operator="-"
            log=returnPrint(num1, operator, num2, "=", subtract(num1, num2))
            print(log)

        elif choice == '3':
            operator="*"
            log=returnPrint(num1, operator, num2, "=", multiply(num1, num2))
            print(log)
            
        elif choice =='4':
            operator="/"
            res=divide(num1, num2)
            log=returnPrint(num1, operator, num2, "=", res)
            if res is not None: 
                print(log)
            else:
                abnormal=True 
                
        if abnormal:
            errorLog(log)
        else:
            Log(log)

        # check if user wants another calculation
        # break the while loop if answer is no
        
        repeat=True
        
        while repeat is True:
            next_calculation = input("Let's do next calculation? (yes/no): ").lower();
            
            if next_calculation == "no":
                answer=input("Are you sure? (yes/no): ").lower();
                if answer == "yes":
                    repeat=False
                    break; 
                elif answer=="no":
                    break;
                else:
                    print("You can only choose yes or no") 
                    repeat=True
            elif next_calculation=="yes":
                break;
            else:
                print("You can only choose yes or no") 
                repeat=True
        
        if repeat is False:
            break;

    else:
        print("Invalid Input")
        log=returnPrint(choice)
        errorLog(log)



#commit test
