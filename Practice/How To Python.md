## Mark Down Cheat Sheet 
[This has **bolding**, *italics*, bullets, link, and quotes](http://nestacms.com/docs/creating-content/markdown-cheat-sheet)

## Writing a program

1. Open python IDLE
2. push ctrl+N to get to the code creation 
3. type
4. save then push F5 to execture 

Code block which represents the body of a function or a loop begins with the indentation and ends with the first unindented line (4 spaces).

[reference](http://www.techbeamers.com/python-tutorial-step-by-step/#silent-features-in-python)

## Python Key Words examples
* **id()** confirms  memory address
* **print()** 
* **type()** tells you the type of variable yopu have. float, integer, 
* %: divisibility
	* [example](https://github.com/brandibushman/Math-4610-USU-Keobbe/blob/master/Practice/else%20if%20.md)


[Keywords] (http://www.techbeamers.com/python-keywords-identifiers-variables/#keywords-in-python)


## Python Statements
Logical instruction which python interpreter can read
* **Expressions:** are a type of python statement which contains a logical sequence of numbers, strings, objects, and operators. 
  * Arithmetic. add +, subtract -, multiply *, divide /, 
  * ***Concatenation*** *(or string concatination)*: the operation of joing character string end to end. 
      * "snow" and "ball" concatinated to be "snowball"
  * eval. eval("2.5.+2.5") would give you 5.0
 * **Simple Assignment Statements:** create new variables. Similar to maple have an = sign. 
 * **Augmented Assignment Statement** =+ 
~~~
>>> mytuple=(10,20,30)
>>> mytuple += (40,50))
SyntaxError: invalid syntax
>>> mytuple += (40,50)
>>> print(mytuple)
(10, 20, 30, 40, 50)


>>> favorite thing= [cats, lionel, math]
SyntaxError: invalid syntax
>>> favorite thing= ['cats', 'lionel', 'math']
SyntaxError: invalid syntax
>>> favoritething= ['cats', 'lionel', 'math']
>>> favoritething += ['cats', 'Brian', 'movies']
>>> print(favoritething)
['cats', 'lionel', 'math', 'cats', 'Brian', 'movies']
>>> 
~~~
* **Multiline**
  * Explicit: to continue your line of code do \ 
~~~
  >>> print(favoritething)
['cats', 'lionel', 'math', 'cats', 'Brian', 'movies']
>>> holla = 8+\
	7
>>> print(holla)
15
~~~
  * Implicit: (),[],{}
~~~
  >>> favoritethings= ['cats', 'lionel', 'math']
>>> math_is=['cool'
	 'importnat']
>>> print(math_is)
['coolimportnat']
~~~
* **open** read it 
* **import(filename.py)** This will have access to all the functinos in that file

## Cool Things I learned on October 3rd
~~~
>>> myfloat = 19.1
>>> cat = 2
>>> new = float (cat)
>>> new
2.0
>>> neww = int (myfloat)
>>> 
>>> new
2.0
>>> neww
19
>>> p = 19.9
>>> q= int (p)
>>> q
19
>>> print(177)
177
>>> print(50*60)
3000
>>> print("50*10=", 50*10)
('50*10=', 500)
>>> print("50 * 10 = ", 50*10)
('50 * 10 = ', 500)
>>> print('50*10 = ' , 50*10 )
('50*10 = ', 500)
>>> print('50*10 = '  50*10 )
SyntaxError: invalid syntax
>>> hi = print('50*10 = ' , 50*10 )
SyntaxError: invalid syntax
>>> hi

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    hi
NameError: name 'hi' is not defined
>>> x = 7
>>> y = =9
SyntaxError: invalid syntax
>>> y = 9
>>> print(x+y)
16
>>> print( " {0} * {1} = {2}".format(x,y,x*y))
 7 * 9 = 63
>>> print("Hola ", "Mundo", sep"--------")
SyntaxError: invalid syntax
>>> print("Hola ", "Mundo", sep="--------")
SyntaxError: invalid syntax
>>> print("Hola", "Mundo", sep="--------")
SyntaxError: invalid syntax
>>> name = "Lionel"
>>> print ("who is a cat? %s" % name)
who is a cat? Lionel
>>> age = 4
>>> print ("Why is %s I am %d ! years old" % (name, age))
Why is Lionel I am 4 ! years old
>>>  print ("Hola", "Mundo", sep="--------")
 
  File "<pyshell#39>", line 2
    print ("Hola", "Mundo", sep="--------")
    ^
IndentationError: unexpected indent
>>> hey = 50*10
>>> print("50*10= %s " % hey)
50*10= 500 
>>> print("cat = %f.4" % 88.2)
cat = 88.200000.4
>>> print("cat = %.4f" % 88.2)
cat = 88.2000
>>> sup = input ("Who is your ho:")
Who is your ho:6
>>> sup
6
>>> IamSoSleepy = ("how many hours do you want to sleep")
>>> IamSoSleepy
'how many hours do you want to sleep'
>>> IamSoSleepy =  input ("how many hours do you want to sleep:")
how many hours do you want to sleep:500
>>> 
~~~
