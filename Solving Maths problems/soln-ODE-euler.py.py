import math

def func(x):
    func = math.sin(x)
    return func

x0 = 0 
xf = 1
y0 = 1
h = 0.1
n = int((xf-x0)/h)

print("x \t y")
print("%.2f \t %.2f"%(x0,y0))
for i in range(1,n+1):
    y0 += h*func(x0)
    x0 += h 
    print("%.2f \t %.2f"%(x0,y0))
