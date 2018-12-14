# Vector Subtraction

**Routine Name:**           VecSub.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    VecSub(u,v)

**Description/Purpose:** Subtracts vectors component wise.

**Input:** Two vectors

**Output:** One Vector as a list. 

**Usage/Example:**
~~~
>>> u = [1,2,3,4,5]
>>> v = [5,4,3,2,1]
>>> VecSub(u,v)
~~~      
Output from the lines above:
~~~
[-4,-2,0,2,4]
~~~

**Implementation/Code:**
 
~~~
def VecSub(u,v):
    length = len(u)
    z = []

    for i in range(length):
        z.append(u[i] - v[i])

    return z

~~~

