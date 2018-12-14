# Matrix Transpose

**Routine Name:**          maxtrans.py

**Author:** Brandi Bushman

**Language:** Python

For example,

  maxtrans(A)


**Description/Purpose:** Swaps rows and columns.

**Input:** Matrix as lists of lists

**Output:** Matrix as lists

**Usage/Example:**
~~~
>>> A = [[1,2,3],[4,5,6],[7,8,9]]
>>> maxtrans(A)
~~~      
Output from the lines above:
~~~
[1,4,7]
[2,5,8]
[3,6,9]
~~~

**Implementation/Code:**
 
~~~
def maxtrans(A):
    row = len(A)
    col = len(A[0])
    trans = []
    for j in range (col):
        rows = []
        for i in range (row):
            element = A[i][j]
            rows.append(element)
        trans.append(rows)

    return transpose

~~~
