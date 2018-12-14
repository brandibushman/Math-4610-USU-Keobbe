
# Secant Method

**Routine Name:** secant.py
 
**Author:** Brandi Bushman
 
**Language:** Python 

For example,

    def Secant(f, x0, x1, tol, maxiter)

**Description/Purpose:** The roots of a function

**Input:** Function, x0, x1, tolerance, max iterations. 


**Output:** The root or a no roor message. 

**Usage/Example:** The routine requires five arguments. The routine returns the approximate root value.

~~~
 Secant(lambda x: x**2 - 3, 1, 4, pow(10, -15), 15)
~~~
Output from the code above:

~~~
1.7320508075688767 
~~~

**Implementation/Code:** The following code is for secant(f, x0, x1, tol, maxIter)

~~~

def Secant(f, x0, x1, tol, maxiter):

    i = 0
    error = 10 * tol

    while(error > tol and i < maxiter):

        i = i + 1
        x2 = x1 - (f(x1)*(x1 - x0))/(f(x1) - f(x0))
        error = abs(x2-x1)
        x0 = x1
        x1 = x2

    return x0
~~~
