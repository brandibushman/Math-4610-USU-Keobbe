# Multiplying a Scalar into a Matrix

**Routine Name:**          maxscalar.py

**Author:** Brandi Bushman

**Language:** Python

For example,

  maxscalar(x,A)


**Description/Purpose:** Multiplies a scalar by each component in the matrix.  

**Input:** A scalar, x, and a matrix, A,  as lists of lists

**Output:** Matrix as list lists

**Usage/Example:**
~~~
>>> A = [[1,2,3],[4,5,6],[7,8,9]]
>>> maxscalar(4,A)
~~~      
Output from the lines above:
~~~
[4,8,12]
[16,20,24]
[28,32,36]
~~~

**Implementation/Code:**
 
~~~
def maxscalar(x,A):
    row = len(A)
    col = len(A[0])

    for i in range(row):
        for j in range(col):
            A[i][j] *= x
  return(A)

~~~
