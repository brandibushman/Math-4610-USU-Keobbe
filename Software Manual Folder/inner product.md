# Vector Subtraction

**Routine Name:**           VecInP.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    VecInP(u,v)

**Description/Purpose:** Find the inner product of two vectors.

**Input:** Two vectors

**Output:** The inner product.

**Usage/Example:**
~~~
>>> u = [1,2,3,4,5]
>>> v = [5,4,3,2,1]
>>> VecInP(u,v)
~~~      
Output from the lines above:
~~~
35
~~~

**Implementation/Code:**
 
~~~
def VecInP(u,v):
    
    length = len(u)
    z = 0.0

    for i in range (length):
        z += u[i] * v[i]
    
    return z

~~~

