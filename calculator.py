def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b0):
    c=a/b
    return c
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
if ch==1:
    x=add(a,b)
    print(x)
elif ch==2:
    x=sub(a,b)
    print(x)
elif ch==3:
    x=mul(a,b)
    print(x)
else:
    x=div(a,b)
    print(x)
