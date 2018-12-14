# Infinity Norm Absolute Error

**Routine Name:**           NormInfAbs.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    NormInfAbs(u,v)


**Description/Purpose:** Finds the length of a vector using infinity norm.

**Input:** Vector in the form of a list. 

**Output:**  Absolute error. 

**Usage/Example:**
~~~
>>> v = [11,22,33,44]
>>> w = [11.1,21.7,33.3,44.12]
>>> NormInfAbs(V)
~~~      
Output from the lines above:
~~~
.0027272727
~~~

**Implementation/Code:**
 
~~~
import Norm2Leng, error_rel, error_abs

def NormInfAbs(v, u):
    lU = Norm2Leng(u)
    lV = Norm2Leng(v)

    return error_abs(lU,lV)
                

~~~
