# Math 4610 Fundamentals of Computational Mathematics Software Manual 

**Routine Name:**           Hello.f
**Author:** Brandi Bushman 

**Language:** Fortran
 
For example,

    Hello.f

will produce an executable **./Hello.exe** than can be executed.

**Description/Purpose:** This routine will have each thread in your computer say Hello world.   

**Input:** Open the executable file 
~~~
A02234836@ENG30352 ~
$ gfortran -fopenmp Hello.f -o Hello

~~~

**Output:** Each thread will say hello and it will count the number of threads your computer has.  

**Usage/Example:** 
~~~
      A02234836@ENG30352 ~
$ ./Hello.exe
 Hello World from thread           6
 Hello World from thread           5
 Hello World from thread           2
 Hello World from thread           1
 Hello World from thread           7
 Hello World from thread           0
 Hello World from thread           3
 Hello World from thread           4
 There are           8 threads!
~~~
      
**Implementation/Code:**
~~~
      program main
      integer id, nthrds
      integer omp_get_thread_num, omp_get_num_threads
C$OMP PARALLEL PRIVATE(id)
      id = omp_get_thread_num()
      print *, 'Hello World from thread' , id
C$OMP BARRIER
      if(id .eq. 0) then
              nthrds = omp_get_num_threads()
              print *, 'There are' , nthrds, 'threads!'
      end if
C$OMP END PARALLEL
      stop
      end
~~~
