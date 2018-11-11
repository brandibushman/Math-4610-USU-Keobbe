# dmaceps
This is a program I will write this weekend, because I'm still struggling

**Routine Name:**           dmaceps()

**Author:** Brandi

**Language:** probably python

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
            
    
def smaceps(): #machine eposilon for 32 bit
    import numpy as np
    eps2 = np.float32(0.5) #typecast as float 32 bits of precision   
      
    while ((1+eps2) != 1): 

        pre = eps2 
        eps2 = eps2 / 2
        
    print( "Machine Epsilon for single is : " , pre )
            

~~~
