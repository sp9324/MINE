divisors_array=[]
sum=0
num=int(input("enter number: "))
for i in range(1, num+1):
    if num%i==0:
        sum+=i


if num==sum/2:
    print("it is a perfect number!!!")
else:
    print("no...")    