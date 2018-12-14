# Vector Addition

**Routine Name:**           VecAdd.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    VecAdd(u,v)

**Description/Purpose:** Adds vectors component wise.

**Input:** Two vectors

**Output:** One Vector as a list. 

**Usage/Example:**
~~~
>>> u = [1,2,3,4,5]
>>> v = [5,4,3,2,1]
>>> VecAdd(u,v)
~~~      
Output from the lines above:
~~~
[6,6,6,6,6]
~~~

**Implementation/Code:**
 
~~~
def VecAdd(u,v):
    length = len(u)
    z = []

    for i in range(length):
        z.append(u[i] + v[i])

    return z

~~~
