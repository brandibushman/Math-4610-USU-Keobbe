# One Norm Lengths
This is a program which will evaluate the double precision epsilon of your computer.

**Routine Name:**           Norm1AbE.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    Norm1AbE()


**Description/Purpose:** COmputes the absolute error of the norm 1. 

**Input:** Input is two vectors put in as  lists one is the exact vector and the other one is the approximated one. 

**Output:**  The absolute error
**Usage/Example:**
~~~
>>> v = [11,22,33,44,55,66,44]
>>> w = [11.1,21.7,33.3,44.12,54.88,66.2,43.83]
>>> Norm1AbE(v,w)
~~~      
Output from the lines above:
~~~
.13
~~~

**Implementation/Code:**
~~~
def Norm1AbE( Exact, Approx ):
    E = 0.0
   for element in Exact:
      E += abs(element)
   for element in Approx:
      A += abs(element)
   
   AbEr = abs(E-A)
   return ( AbEr)
                
~~~
