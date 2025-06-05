def fib(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        a=0
        b=1
        for i in range(2,n):
            a,b=b,a+b
    

x=fib(5)
print(x)