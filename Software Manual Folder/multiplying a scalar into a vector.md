# Vector Scalar Multiplication
**Routine Name:**           VecScalar.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    VecScalar(x,u)

**Description/Purpose:** Multiplies a scalar by each componenet in the vector.

**Input:** A scalar, x, and a vector, u. 

**Output:** One Vector as a list. 

**Usage/Example:**
~~~
>>> u = [1,2,3,4,5]
>>> VecSub(3,u)
~~~      
Output from the lines above:
~~~
[3,6,9,12,15]
~~~

**Implementation/Code:**
 
~~~
def VecScalar(x,u):
  for i in range(len(x)):
        
        x[i] *= scalar

~~~

