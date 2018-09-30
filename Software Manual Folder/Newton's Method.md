# Relative Error Calculator
Uses the Newton Method to find roots

**Routine Name:**           NewtonMethod

**Author:** Brandi Bushman

**Language:** Python, python compiler

For example,

  NewtknMetho(x , f , g , tol, maxiter):


**Description/Purpose:** This routine will find a root of the function entered. 

**Input:** x is the closeness you want to the root. f is the function, g is the derivative of the function.  

**Output:** Ta root of the euqaiton. 
**Usage/Example:**

~~~

~~~

Output from the lines above:

~~~

~~~

This value represents a root of the funciton |x| error. 

**Implementation/Code:** The following is the code for error_rel()
~~~
def NewtonMethod( x , f , g, tol, maxiter ):
    h = f.subs( 'x' = x ) / g.subs('x' = x )
    while abs(h) >= .0001:
        h = f / g
        x= x - h
    return(x) 
~~~
