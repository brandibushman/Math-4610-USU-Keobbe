
# Secant Method

**Routine Name:** secant.py
 
**Author:** Brandi Bushman
 
**Language:** Python 

For example,

    def secant(f, x0, x1, tol, maxiter)

**Description/Purpose:** The roots of a function

**Input:** Function, x0, x1, tolerance, max iterations. 


**Output:** The root. 

**Usage/Example:** The routine requires five arguments. The routine returns the approximate root value.

~~~
>>> f = x**2 - 3
>>> secant(f,0, 2, pow(10,-11), 11)
~~~
Output from the code above:

~~~
1.7320508075688767 
~~~

**Implementation/Code:** The following code is for secant(f, x0, x1, tol, maxIter)

~~~

def secant(f, x0, x1, tol, maxiter):

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
