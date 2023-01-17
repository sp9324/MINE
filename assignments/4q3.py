import random

i=1
while i<=10:
    num1=random.randint(0,9)
    num2=random.randint(0,9)
    answer=int(input("Question i: print(num1) * print(num2)="))
    if answer==num1*num2:
        print("Right!")
    else:
        print("Wrong. The answer is num1*num2.") 
    i+=1

