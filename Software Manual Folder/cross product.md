# Vector Cross Product

**Routine Name:**           VecCross.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    VecCross(u,v)

**Description/Purpose:** Find the corss product of two vectors.

**Input:** Two vectors

**Output:** The cross product vector.

**Usage/Example:**
~~~
>>> u = [1,2,3,4,5]
>>> v = [5,4,3,2,1]
>>> VecCross(u,v)
~~~      
Output from the lines above:
~~~

~~~

**Implementation/Code:**
 
~~~
def VecCross(u,v):

    x = (u[1] * v[2]) - (u[2] * v[1])
    y = (u[2] * v[0]) - (u[0] * v[2])
    z = (u[0] * v[1]) - (u[1] * v[0])
    
    return [x,y,z]
    
~~~

