# One Norm Lengths
This is a program which will evaluate the double precision epsilon of your computer.

**Routine Name:**           NormInfLeng.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    NormInfLegth()


**Description/Purpose:** Finds the length of a vector.

**Input:** Vector in the form of a list. 

**Output:**  Length of vector or list by identifying the largest element of the vector or list.

**Usage/Example:**
~~~
>>> v = [5,99,32,1.44,5.1,22,33,44,88,55]
>>> NormInfLeng(V)
~~~      
Output from the lines above:
~~~
99
~~~

**Implementation/Code:**
 
~~~
def NormInfLeng(v):
  
  L = max(v)

  return(float(L))
                

~~~

