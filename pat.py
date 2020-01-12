n=int(input("enter limit"))
n=n//2
a=0
for i in range(n,-1,-1):
    for j in range(i):
        print("#",end="")
    for k in range(0,1):
        print("*"*a,end="")
    for j in range(i):
        print("#",end="")
    a=a+2
    print()
a=a-4
for i in range(1,n+1):
    for j in range(i):
        print("#",end="")
    for k in range(0,1):
        print("*"*a,end="")
    for j in range(i):
        print("#",end="")
    a=a-2
    print()