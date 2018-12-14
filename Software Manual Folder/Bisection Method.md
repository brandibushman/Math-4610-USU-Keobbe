# Bisection Method

**Routine Name:**           bisect.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    bisect(f,a,b,tol, maxiter)


**Description/Purpose:** Find the roots of a function using subintervals. 

**Input:** Function, two boounds, and tolerance, and max number of iterations. 

**Output:** Roots, if they exist. 

**Usage/Example:**
~~~
>>> f = x**2 - 3
>>> bisect(f,0, 2, pow(10,-11), 11)
~~~      
Output from the lines above:
~~~
1.73205079
~~~

**Implementation/Code:**

~~~
def bisect( f, a , b , tol , maxiter):
    h = subs.f( x = a )
    g = subs.f( x = b )
    if h* g  > 0
        return(True)
    else:
        return(False)
~~~
