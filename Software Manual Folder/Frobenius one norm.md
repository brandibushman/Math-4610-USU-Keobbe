# Frobenius One Norm

**Routine Name:**          Fr1Norm.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    Fr1Norm(A)


**Description/Purpose:** Adds right most columns 

**Input:** A matrix which is a list of lists. 

**Output:** Frobenius One Norm.

**Usage/Example:**
~~~
>>> A = [[11,22,33],[1,2,3],[4,5,16]]
>>> Fr1Norm(A)
~~~      
Output from the lines above:
~~~
42
~~~

**Implementation/Code:**
 
~~~

 def OneNorm(A):
    row = len(A)
    col = len(A)
    norm = 0.0
    colSum = []

    for j in range(col):
        for i in range(row):
            norm += abs(A[i][j])
        colSum.append(norm)
        norm = 0.0
    
    norm = max(colSum)
    return norm               

~~~
