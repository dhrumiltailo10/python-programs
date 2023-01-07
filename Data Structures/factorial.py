
x = int(input("enter the number whose factorial you need : "))

def factorial (x):
    if x == 1:
     return 1
    else:
        return (x*factorial(x-1))

print("the factorial of %.1f is %.1f"%(x, factorial(x)))

def factorial1(x):
    y=1
    for i in range(1, x+1):
        y = y*i
    return y

print("the factorial of %.1f is %.1f"%(x, factorial1(x)))