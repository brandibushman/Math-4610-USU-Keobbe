# Vector Matrix multiplication

**Routine Name:**          vecmmat.py

**Author:** Brandi Bushman

**Language:** Python

For example,

  vecmmat(A,u)


**Description/Purpose:** Multiplies a row vector by a matrix. 

**Input:** A vector as a list, length n, and a matricies as lists of lists, m,n dimensions. 

**Output:** Vector as a list.

**Usage/Example:**
~~~
>>> u = [3,2,1]
>>> A = [[1,2,3],[4,5,6],[7,8,9]]
>>> vecmmat(A,u)
~~~      
Output from the lines above:
~~~
[10,28,91]
~~~

**Implementation/Code:**
 
~~~
def vecmmat(A,u):
    row = len(A)
    col = len(A[0])
    product = [0]*row
    for j in range(col):
        rows = []
        for i in range(row):
            rows.append(A[i][j])
        
        scalar(rows, u[j])
        for i in range(row):
            product[i] += rows[i]
        
    return product

~~~
