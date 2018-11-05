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
 
def dmaceps():
    EPS = .9
  
    while ((1+EPS) != 1): 

        prev_epsilon = EPS 
   

        EPS = EPS / 2
   

    print( "Machine Epsilon is : " , 
            prev_epsilon )
