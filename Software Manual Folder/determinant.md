# Determinant

**Routine Name:**           det.py

**Author:** Brandi Bushman

**Language:** Python

For example,

  det(A)


**Description/Purpose:**  Finds the determinant of a matrix. 

**Input:** A matrix as lists of lists.

**Output:** The determinant. 

**Usage/Example:**
~~~
>>> A = [[1,2,3],[0,4,5],[0,0,1]]
>>> det(A)
~~~      
Output from the lines above:
~~~
4
~~~

**Implementation/Code:**
 
~~~
def det(A):
    d = 0.0
    n = len(A[0])
    Upper(A,([0]*n))
    d = Trace(A)
    return d
~~~

