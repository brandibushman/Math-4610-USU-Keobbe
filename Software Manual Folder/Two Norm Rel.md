# Two Norm Relative Error

**Routine Name:**           Norm2Rel.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    Norm2Rel(u,v)


**Description/Purpose:** Finds the length of a vector using two nrom.

**Input:** Vector in the form of a list. 

**Output:**  Length of vector or list by taking the square root of the sum of the squares of the elements. 

**Usage/Example:**
~~~
>>> v = [11,22,33,44]
>>> w = [11.1,21.7,33.3,44.12]
>>> Norm2Rel(V)
~~~      
Output from the lines above:
~~~
.0053602038
~~~

**Implementation/Code:**
 
~~~
import Norm2Leng, error_rel, error_abs

def Norm2Rel(v, u):
    lU = Norm2Leng(u)
    lV = Norm2Leng(v)

    return error_rel(lU,lV)
                

~~~
