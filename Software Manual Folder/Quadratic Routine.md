# Math 4610 Fundamentals of Computational Mathematics Software Manual
This is the logic I plan on using for this assignment. Then create a shared file. 

**Routine Name:**           quad

**Author:** Brandi

**Language:** Python

For example,

    quadratic.py

**Description/Purpose:** This routine will take values a,b,c which are the coefficients for a quadratic polynomial then compute the roots.

**Input:** In put variables are the coefficients to the quadratic equation ax^2 + bx +c

**Output:** This routine returns an array with two entries for when we add the square root of the discriminant and when we subtract the square root of the discriminant.


**Usage/Example:** information here
    >>> quad(1,-1,-6)
    
     
Output from the lines above:

      [3.0, -2.0]
      
**Implementation/Code:**
    def quad(a,b,c):

    d = ((b*b) - (4*a*c))
    if d<0:
         print('Not real!!!')    
    else:
        import math
        z = math.sqrt(d)
        
        x1 = (-b + z)/(2*a)
        x2 = (-b - z)/(2*a)
    from array import array
    my_array = [x1,x2]
    return my_array



