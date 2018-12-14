# Approximating the Derivative

**Routine Name:**           approxder.py

**Author:** Brandi Bushman

**Language:** Python, python compiler

For example,

  approxder(x,y,h)


**Description/Purpose:** This routine will apporximate the area under the curve of  f(x)=x<sup>2</sup> from y to x by using the defintion of the integral, where h  is the "wdith" of the retangles under the curve. 

**Input:** The first input number, x, is the upper bound of our integration and our second input value, y, is the lower bound. Out last input number, h, is the width.  

**Output:**One value, the approximation of the integral x<sup>2</sup> from y to x. 

**Usage/Example:**
[example with approximation]()
~~~
>>> approxder(3,2,.01)
~~~

Output from the lines above:

~~~
1.9999999999999574
~~~

This value represents the absolute value of the difference between the two answers. 

**Implementation/Code:** The following is the code for error_abs()
~~~
def approxder( x, y, h):
    R = ((((x+h)**2 - x**2)-((y+h)**2 - y**2))/h)  
    return(R)
~~~

**Last Modified:** September/2019

~~~
def approxder(x, y, h):
    return (y(x+h) - y(a))/h


~~~
