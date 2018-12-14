# Two Norm Lengths

**Routine Name:**           Norm2AbE.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    Norm2AbE()


**Description/Purpose:** Computes the absolute error of two vectors with the norm 2. 

**Input:** Two vectors one exact and one an approximation. Must be put in as lists. 

**Output:**  The absolute error
**Usage/Example:**
~~~
>>> v = [11,22,33,44]
>>> w = [11.1,21.7,33.3,44.12]
>>> Norm2AbE(v,w)
~~~      
Output from the lines above:
~~~
.1574719166
~~~

**Implementation/Code:**
~~~
import Norm2Leng, error_rel, error_abs

def Norm2Abs(v, u):
    lU = Norm2Leng(u)
    lV = Norm2Leng(v)

    return error_abs(u,v)
                
~~~
