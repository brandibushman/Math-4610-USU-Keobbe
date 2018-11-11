# smaceps
This is a program which will evaluate the single precision epsilon of your computer.

**Routine Name:**           smaceps()

**Author:** Brandi Bushman

**Language:** Python

For example,

    smaceps.py


**Description/Purpose:** This will return then numerical value for single mechine precision for floating points. 
**Input:** none

**Output:** Machine precision number which demonstrates how many decimal digits are precise. 

**Usage/Example:**

     >>> smaceps()
      
Output from the lines above:

    ('Machine Epsilon is : ', 1.9984013913857226e-16)
      
**Implementation/Code:**
 
~~~

def smaceps(): #machine eposilon for 32 bit
    import numpy as np
    eps2 = np.float32(0.5) #typecast as float 32 bits of precision   
      
    while ((1+eps2) != 1): 

        pre = eps2 
        eps2 = eps2 / 2
        
    print( "Machine Epsilon for single is : " , pre )
            

~~~
