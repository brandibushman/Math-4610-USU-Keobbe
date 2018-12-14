# Hybrid Secant

**Routine Name:** newsec.py
 
**Author:** Brandi Bushman
 
**Language:** Python 

For example,

    newsec(f, a , b, tol, maxiter)

**Description/Purpose:** The roots of a function

**Input:** Function, bounds, tolerance, max iterations. 


**Output:** The root. 

**Usage/Example:** The routine requires five arguments. The routine returns the approximate root value.

~~~
>>> f = x**2 - 3
>>> newsec(f,0, 2, pow(10,-11), 11)
~~~
Output from the code above:

~~~
1.7320508075688767 
~~~

**Implementation/Code:** The following code is for secant(f, a , b , tol, maxIter)

~~~

def newsec(f, a, b, tol, maxiter):
    i = 0
    sec = None
    x = bisection.bisection(f, a, b, tol, 4)
    xa = x[0]
    xb = x[1]
    if(x is None):
        return None
    while (i < maxIter):
        i += 1
        sec = secant.Secant(f,xa, xb,tol,maxIter)
        if(sec is not None):
            return sec
        else:
            x = bisection.bisection(f, xa, xb, tol, 4)
            xa = x[0]
            xb = x[1]
    return(sec)
~~~

