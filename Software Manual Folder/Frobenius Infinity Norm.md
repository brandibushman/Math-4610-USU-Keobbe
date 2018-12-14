# Frobenius Infinity Norm

**Routine Name:**          FrInfNorm.py

**Author:** Brandi Bushman

**Language:** Python

For example,

    FrInfNorm(A)


**Description/Purpose:** Adds the largest values of each column.

**Input:** A matrix which is a list of lists. 

**Output:** Frobenius Infinity Norm.

**Usage/Example:**
~~~
>>> A = [[11,22,33],[1,2,3],[4,5,16]]
>>> FrInfNorm(A)
~~~      
Output from the lines above:
~~~
66
~~~

**Implementation/Code:**
 
~~~

def FrInfNorm(A):
    row = len(A)
    col = len(A)
    norm = 0.0
    rowSum = []

    for i in range(row):
        for j in range(col):
            norm += abs(matrix[i][j])
        rowSum.append(norm)
        norm = 0.0
    
    norm = max(rowSum)
    return norm         

~~~
