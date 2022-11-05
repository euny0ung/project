# Program make a simple calculator

from io import StringIO
from main_func import *
from log_func import *
    
# print 값을 변수에 저장하기 위한 함수
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

    # 입력에 숫자가 아닌 다른 수가 들어오는 케이스를 구분하는 변수
    retry=True

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        
        # 정상적인 연산처리를 구분하는 변수
        abnormal=False
        
        # 입력에 숫자 이외의 값이 들어오는 경우 예외처리
        while retry is True:
            try:
                firstNum = float(input("Enter first number: "))
                secondNum = float(input("Enter second number: "))
            except:
                retry=True
                num1=None
                num2=None
                print("You can only enter numbers")
            else: 
                retry=False
                num1=firstNum
                num2=secondNum

        # 입력 결과가 정상일 때만 연산 수행
        if num1 is not None and num2 is not None:
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
                  
            # 정상적으로 수행한 경우와 비정상적으로 수행한 경우를 각각 다른 파일에 기록
            if abnormal:
                errorLog(log)
            else:
                Log(log)
            
            repeat=True

            # yes, no 외의 다른 값이 들어올 경우 재실행
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

    # 1, 2, 3, 4 외에 다른 값이 들어올 경우 errorLog에 기록
    else:
        print("Invalid Input")
        log=returnPrint(choice)
        errorLog(log)



#commit test
