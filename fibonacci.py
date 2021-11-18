#fibonacci series
a=0
b=1
n=int(input("Enter the number of fibonacci to be generated:"))
if n<=0:
    print("Not possible")
elif n==1:
    print(a)
elif n>=2:
    print("The fibonacci series is:")
    for i in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c
        
            
