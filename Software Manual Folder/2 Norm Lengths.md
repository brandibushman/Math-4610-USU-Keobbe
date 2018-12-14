# Two Norm Lengths

**Routine Name:**           Norm2Leng.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    Norm2Legth()


**Description/Purpose:** Finds the length of a vector using two nrom.

**Input:** Vector in the form of a list. 

**Output:**  Length of vector or list by taking the square root of the sum of the squares of the elements. 

**Usage/Example:**
~~~
>>> v = [5,99,32,1.44,5.1,22,33,44,88,55]
>>> Norm12eng(V)
~~~      
Output from the lines above:
~~~
158.60669468847
~~~

**Implementation/Code:**
 
~~~
def Norm2Leng(v):
    L = 0.0
    for element in vector:
        L += abs(element) * abs(element)
        H = L**(1/2)
    return(H)
                

~~~
