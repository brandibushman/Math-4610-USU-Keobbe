
# Hybrid Newton Method

**Routine Name:** newnext.py
 
**Author:** Brandi Bushman
 
**Language:** Python 

For example,

    newnext(f, g, a, b, tol, maxiter)

**Description/Purpose:** The roots of a function

**Input:** Function, derivative of the function, bounds, tolerance, max iterations. 


**Output:** The root. 

**Usage/Example:** The routine requires five arguments. The routine returns the approximate root value.

~~~

~~~
Output from the code above:

~~~

~~~

**Implementation/Code:** The following code is for secant(f, x0, x1, tol, maxIter)

~~~
def newnewt(f, g, a, b, tol, maxiter):

    error = 10 * tol
    i = 0
    new = None    
    x = bisection.bisection(f, a, b, tol, 4)
    xa = x[0]
    xb = x[1]
    if(x is None):
        return None
    while (i < maxiter):
        i += 1
        x0 = .5*(xa + xb)  
        newton = newtonMethod.NewtonMethod(f,g, x0, tol, maxiter)
        if(newton is not None):
            return newton
        else:
            x = bisection.bisection(f, xa, xb, tol, 4)
            xa = x[0]
            xb = x[1]
    return new
~~~
