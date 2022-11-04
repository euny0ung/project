# Program make a simple calculator

from io import StringIO

# This function adds two numbers
def add(x, y):
    return x+y

# This function subtracts two numbers
def subtract(x, y):
    return x-y


# This function multiplies two numbers
def multiply(x, y):
    return x*y

#Need to define divide function.
def divide (x,y):
    try:
        result=x/y
        return result
    except ZeroDivisionError:
        print("You can't divide it by zero")
        return None

def Log(newLog):
    f=open("./log.txt", "a")
    f.write(newLog)
    f.close()
    
def errorLog(newLog):
    f=open("./errorLog.txt", "a")
    f.write(newLog)
    f.close()
    
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
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

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
            if res is not None: 
                log=returnPrint(num1, operator, num2, "=", res)
                print(log)
            else:
                log=returnPrint(num1, operator, num2, "=", res)
                abnormal=True 
                
        if abnormal:
            errorLog(log)
        else:
            Log(log)

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ").lower();
        
        # if next_calculation == "no":
        #     answer=input("Are you sure? (yes/no): ").lower();
        #     if answer == "yes":
        #         break;
        #     elif answer=="no":
        #         continue;
        # elif next_calculation=="yes":
        #     continue;
        # else:
        #     print("You can only choose yes or no")
        #     # 재확인 루틴 개발중
        
        if next_calculation == "no":
            answer=input("Are you sure? (yes/no): ").lower();
            if answer == "yes":
                break;
            if answer=="no":
                continue; 

    else:
        print("Invalid Input")
        log=returnPrint(choice)
        errorLog(log) ###개행 들어가야함



#commit test
