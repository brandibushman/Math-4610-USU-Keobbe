# Relative Error Calculator
This routine can calculate absolute and relative error.

**Routine Name:**           error_rel

**Author:** Brandi Bushman

**Language:** Python, python compiler

For example,

  error_rel(x,y)


**Description/Purpose:** This routine will produce the relative error of two numbers entered into it. 

**Input:** The first number, x, is the mechine precision number. The second number,y, is the exact value. 

**Output:** The absolute error. 

**Usage/Example:**

~~~
>>> error_rel(-1.5,-1.2)
~~~

Output from the lines above:

~~~
0.20000000000000004
~~~

This value represents the absolute value of the difference between the two answers, divided by the mechine precision. 

**Implementation/Code:** The following is the code for error_rel()
~~~
def error_rel(x,y):
    A=(abs(x-y))/(abs(x))
    return (A)
~~~
