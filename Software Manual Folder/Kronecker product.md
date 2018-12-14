# Kronecker Product

**Routine Name:**           kron.py

**Author:** Brandi Bushman

**Language:** Python

For example,

  kron(A,B)


**Description/Purpose:**  Finds the outter product or kronecker product of two matricies. 

**Input:** Two matricies as a list of lists

**Output:** matrix as lists

**Usage/Example:**
~~~
>>> A = [[1,2],[3,4],[5,6]]
>>> B = [[5,6],[3,4],[1,2]]
>>> kron(A,B)
~~~      
Output from the lines above:
~~~
[5,6,10,12]
[3,4,6,8]
[1,2,2,4]
[15,18,20,24]
[9,12,12,16]
[3,6,4,8]
[25,30,30,36]
[15,20,18,24]
[5,10,6,12]
~~~

**Implementation/Code:**
 
~~~
def kron(A,B):
    m = len(A[0])
    n = len(A)

    p = len(B[0])
    q = len(B)
    
    C = [[0 for i in range(m*p)] for i in range(n*q)]

    for i in range (m):

        for k in range(p):
        
            for j in range(n):

                for l in range(q):

                    C[i + l + 1][j+k +1] = A[i][j] * B[k][l]
    
    return C
~~~

