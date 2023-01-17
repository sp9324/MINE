x=int(input("enter first side:"))
y=int(input("enter second side:"))
z=int(input("enter third side:"))
if x+y<z or y+z<x or x+z<y:
    print("no")
else:
    print("yes")    
