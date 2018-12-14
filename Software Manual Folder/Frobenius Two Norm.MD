# Frobenius Norm

**Routine Name:**          FrNorm.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    FrNorm(A)


**Description/Purpose:** Adds right most columns 

**Input:** A matrix which is a list of lists. 

**Output:** Frobenius Norm.

**Usage/Example:**
~~~
>>> A = [[11,22,33],[1,2,3],[4,5,16]]
>>> FrNorm(A)
~~~      
Output from the lines above:
~~~
44.77722635
~~~

**Implementation/Code:**
 
~~~

def FrNorm(matrix):
    row = len(A)
    col = len(A[0])
    norm = 0.0

    for i in range(row):
        for j in range(col):
            norm += abs(A[i][j] * A[i][j])
    norm = norm**(.5)

    return norm              

~~~
