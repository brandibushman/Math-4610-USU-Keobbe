# Trace of a Matrix

**Routine Name:**          trace.py

**Author:** Brandi Bushman

**Language:** Python

For example,

  trace(A)


**Description/Purpose:** Sum along the diagonal. 

**Input:** Matrix as lists of lists

**Output:** Trace. 

**Usage/Example:**
~~~
>>> A = [[1,2,3],[4,5,6],[7,8,9]]
>>> trace(A)
~~~      
Output from the lines above:
~~~
15
~~~

**Implementation/Code:**
 
~~~
  row = len(A)
  trace = 0.0
  for i in range(row):
      trace += A[i][i]
  return trace

~~~
