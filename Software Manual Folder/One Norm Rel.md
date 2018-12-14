# One Norm Relative Error
This is a program which will evaluate the double precision epsilon of your computer.

**Routine Name:**           Norm1Rel.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    Norm1Rel(u,v)


**Description/Purpose:** Finds the relative error of two vectors by looking at their length. 

**Input:** The exact vector, v, and the apporximated one, u.

**Output:**  Relative error.  

**Usage/Example:**
~~~
>>> v = [11,22,33,44]
>>> u = [10.8,22.3,33.4,43.65]
>>> Norm1LRel(u,v)
~~~      
Output from the lines above:
~~~
.15
~~~

**Implementation/Code:**
 
~~~
import Norm1Leng, error_rel

def Norm1Rel(v, u):
    lU = Norm1Leng(u)
    lV = Norm1Leng(v)

    return error_rel(u,v)
                

~~~
