# Infinity Norm Relative Error

**Routine Name:**           NormInfRel.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    NormInfRel(u,v)


**Description/Purpose:** Finds the length of a vector using infinity norm.

**Input:** Vector in the form of a list. 

**Output:**  Relative error. 

**Usage/Example:**
~~~
>>> v = [11,22,33,44]
>>> w = [11.1,21.7,33.3,44.12]
>>> NormInfRel(V)
~~~      
Output from the lines above:
~~~
.12
~~~

**Implementation/Code:**
 
~~~
import Norm2Leng, error_rel, error_abs

def Norm2Rel(v, u):
    lU = Norm2Leng(u)
    lV = Norm2Leng(v)

    return error_rel(lU,lV)
                

~~~
