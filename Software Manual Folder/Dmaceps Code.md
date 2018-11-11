# dmaceps
This is a program which will evaluate the double precision epsilon of your computer.

**Routine Name:**           dmaceps()

**Author:** Brandi Bushman

**Language:** Python

For example,

    dmaceps.py


**Description/Purpose:** This will return then numerical value for double mechine precision for floating points. 
**Input:** none

**Output:** Machine precision number which demonstrates how many decimal digits are precise. 

**Usage/Example:**

     >>> dmaceps()
      
Output from the lines above:

    ('Machine Epsilon is : ', 1.9984014443252818e-16)
      
**Implementation/Code:**
 
~~~
def dmaceps():#machine epsilon for 64 bit
    
    import numpy as np
    eps1 = np.float64(0.5)  #type cast as float, 64 bit precision  
      
    while ((1+eps1) != 1): 

        prev = eps1 
        eps1 = eps1 / 2
        
    print( "Machine Epsilon for double is: " , prev )
            

~~~
