# One Norm Lengths

**Routine Name:**           Norm1Leng.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    Norm1Legth()


**Description/Purpose:** Finds the length of a vector using the one norm.

**Input:** Vector in the form of a list. 

**Output:**  Length of vector. 

**Usage/Example:**
~~~
>>> v = [5,99,32,1.44,5.1,22,33,44,88,55]
>>> Norm1Leng(V)
~~~      
Output from the lines above:
~~~
384.54
~~~

**Implementation/Code:**
 
~~~
def Norm1Leng(v):
    L = 0.0
    for element in vector:
        L += abs(element)

    return(L)
                

~~~
