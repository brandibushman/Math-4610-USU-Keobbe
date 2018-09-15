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
