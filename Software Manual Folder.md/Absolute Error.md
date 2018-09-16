# Error Calculator
This routine can calculate absolute and relative error.

**Routine Name:**           error_abs

**Author:** Brandi Bushman

**Language:** Python, python compiler

For example,

  error_abs(x,y)


**Description/Purpose:** This routine will produce the absolute error of two numbers entered into it. 

**Input:** The first number, x, is the mechine precision number. The second number,y, is the exact value. 

**Output:** The absolute error. 

**Usage/Example:**

~~~
>>> error_abs(-1.5,-1.2)
~~~

Output from the lines above:

~~~
0.30000000000000004
~~~

This value represents the absolute value of the difference between the two answers. 

**Implementation/Code:** The following is the code for error_abs()
~~~
def error_abs(x,y):
    A=abs(x-y)
    return (A)
~~~

**Last Modified:** September/2019
