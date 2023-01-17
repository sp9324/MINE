x = int(input("enter first number: "))
y = int(input("enter second number: "))
z = int(input("enter third number: "))
if (x >= y) and (x >= z):
    largest = x
elif (y >= x) and (y >= z):
    largest = y
else:
    largest = z

print("The largest number is", largest)
