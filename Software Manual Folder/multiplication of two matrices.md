# Matrix Multiplication

**Routine Name:**          matmul.py

**Author:** Brandi Bushman

**Language:** Python

For example,

  matmul(A,B)


**Description/Purpose:** Multiplies matricies component wise. 

**Input:** Two matricies as lists of lists

**Output:** Matrix as list lists

**Usage/Example:**
~~~
>>> A = [[1,2,3],[4,5,6],[7,8,9]]
>>> B = [[9,8,7],[6,5,4],[3,2,1]]
>>> matmul(A,B)
~~~      
Output from the lines above:
~~~
[30,24,18]
[84,69,54]
[138,114,90]
~~~

**Implementation/Code:**
 
~~~
def matmul(A,B):
    row = len(A)
    col = len(B[0])
    m = len(A[0])
    
    C = [[0] * row for i in range(col)]
    
    for i in range(row):
        for j in range(col):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

~~~
