import datetime

def get_current_datetime():
    current_datetime=datetime.datetime.now()
    formatted_datetime=current_datetime.strftime("%d%m%Y,%H:%M:%S")
    print(formatted_datetime )
def divide_numbers():
    while True:
        try:
            num_1=int(input("Enter the divident:"))
            num_2=int(input("Enter a divisor:"))
            result=num_1/num_2
        except ZeroDivisionError:
            print("Errorr: Division by zero is not allowed")
        else:
            pass
        finally:
            print("the code is executed successfully...!!")
            repeat = input("Do ypu want to  perform another division? (yes/no):").strip().lower()
            if repeat != 'yes':
                print(" ")
                break
divide_numbers()
        