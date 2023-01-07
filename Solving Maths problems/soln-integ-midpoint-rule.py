# Mid point method for integration
#import math package
import math
#define parameters
N = 100 # N is the total number of intervals(rectangles) into which the curve under integration is divided (the more the better)
a = 0 # a is the lower limit of the curve to be integrated
b = 1 # b is the upper limit of the curve to be integrated

def integrate (N, a, b):
    def f(x):
        f = x**(-1/2)
        return f
    y_value = 0
    Tot_area = 0

    for n in range(1, N+1):
        x_bar = a + (2*n-1)*(b-a)/(2*N)
        y_value = y_value + f(x_bar)
    Tot_area = y_value*(b-a)/N
    return Tot_area
print ("the solution of integration using Mid-point rule is")
print (integrate (N, a, b))
    
