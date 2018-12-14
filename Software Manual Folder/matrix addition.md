# Matrix Addition

**Routine Name:**          maxadd.py

**Author:** Brandi Bushman

**Language:** Python

For example,

  maxadd(A,B)


**Description/Purpose:** Adds matricies component wise. 

**Input:** Two matricies as lists of lists

**Output:** Matrix as list lists

**Usage/Example:**
~~~
>>> A = [[1,2,3],[4,5,6],[7,8,9]]
>>> B = [[9,8,7],[6,5,4],[3,2,1]]
>>> maxadd(A,B)
~~~      
Output from the lines above:
~~~
[10,10,10]
[10,10,10]
[10,10,10]
~~~

**Implementation/Code:**
 
~~~
def maxadd(A,B):
    row = len(A)
    col = row
    C = [[0]* row for _ in range(row)]
    for i in range(row):
        for j in range(col):
            C[i][j] = A[i][j] + B[i][j]
    return C


~~~
