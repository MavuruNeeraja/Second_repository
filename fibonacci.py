a=int(input("Enter number:"))
x=0
y=1
print(x)
for i in range(a):
    temp=x+y
    x=y
    y=temp
    print(temp)
    
