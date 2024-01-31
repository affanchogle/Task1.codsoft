def addition(num1,num2):
    add=num1+num2
    print(f"Addition of {num1} and {num2} is {add}")

def subtraction(num1,num2):
    sub=num1-num2
    print(f"Subtraction of {num1} and {num2} is {sub}")

def multiplication(num1,num2):
    mul=num1*num2
    print(f"Multiplication of {num1} and {num2} is {mul}")

def division(num1,num2):
    div=num1/num2
    print(f"Division of {num1} and {num2} is {div}")
while True:
    print("   ")
    start=input("Type start/end:")
    if  start == 'start':
        print("_________________________________")
        print("        ")
    elif start =='end':
        break
    else:
        print("error")
    
    choice=input("Enter Your choice:(+,-,*,/):")
    num1=int(input("Enter first value:"))
    num2=int(input("Enter second value:"))

    if choice == '+':
        addition(num1,num2)
    elif choice == '-':
        subtraction(num1, num2)
    elif choice == '*':
        multiplication(num1, num2)
    elif choice =='/':
        division(num1, num2)
    else:
        print("Enter valid choice !")
print(" ")
print("Goodbye")