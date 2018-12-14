# Newton's Method
Uses the Newton Method to find roots

**Routine Name:**           NewtonMethod

**Author:** Brandi Bushman

**Language:** Python, python compiler

For example,

  NewtonMethod(x , f , g , tol, maxiter)


**Description/Purpose:** This routine will find a root of the function entered. 

**Input:** x is the closeness you want to the root. f is the function, g is the derivative of the function.  

**Output:** The root of the equaiton. 
**Usage/Example:**

~~~
>>> f = math.sin(math.radians(x * math.pi))
>>> g = math.cos(math.radians(x * math.pi))
>>> NewtonMethod(0,f,g,pow(10, -15), 15)
~~~

Output from the lines above:

~~~

~~~

This value represents a root of the funciton |x| error. 

**Implementation/Code:** The following is the code for error_rel()
~~~
def NewtonMethod(x , f , g , tol, maxiter):    
    i = 1
    error = 10 * tol
    while (error > tol and i <= maxiter):
        i = i + 1
        x1 = x - f(x)/g(x)
        error = abs(x1 - x)
        x = x1
    if i == maxIter:
        print("No root")
        return None
    else: return x 
~~~
