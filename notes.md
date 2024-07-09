# python:

1. Basics:
   variables
   Datatypes
   Functions
   Control Statements

2. OOPS:
   class
   object
   Inheritance
   polymorphism
   Abstraction..

3. Exceptions
   Multi Threading
   File Handling

4. Pandas:

5. filtering and ordering
6. Grouping(Aggregating):min,max,count,mean,sum and GroupBy
7. Indexing
8. Joins,Merge and concat
9. visualize

10. Numpy

CASE STUDY

# variables:

memory holder
holds singular value
python is type inference->no need to declare the datatype

# declare variable:

a=10;
print(a)
print(id(a))-> displays the memory location
everything is an object in python
in above example a is an object

# datatypes:

1. string
2. int
3. float
4. boolean
5. list--->
   accepts heterogeneous type of data.  
   it can add,update and delete the value.
   starts with []
   a=[10,30,'hii',10.2]
   a.insert(2,20)
   a.append(100)
   a[2]=100
   a.remove('hii')
   a.pop()//removes the last element
   a.pop(2)//removes by index
   print(a.count(value))
   print(len(a))
   a.extend(b)
6. tuple:
   restricted
   ()
   only count and indexes are performed
7. set:
   {}
   no duplicates
   unordered collecttion
   no index
8. dict:
   pair of values.
   {}
   key and value
   d={10:'avh',20:'wer'}
   print(d[20])
   print(d.get(20))

# conditional Statements:

1. conditional statements:
   if
   if else
   else if
   nested if else

2. Looping:
   for->for each
   goes for fixed no .of interarions
   while
   fixed iterations

# for:

a=[10,20,30,40]
for i in a:
print(i)

# while:

i=0;
while i<len(a1):
print(a[i])
i++

#

a=int(input('enter a number'))
print(a)

# class 2:

# functions:

stores the multiple statements
code resuseability

## syntax:

### static:

def add(): ---> defining the function
a=10;
b=20
print(a+b)

add() --->calling the function

### dynamic:

def add(a,b):
print(a+b)

add(10,20) ---> calling a function

### calling from one file to another:(package)

##### from same path: (same folder)

import calc
(or)
from calc(file_name) import add(function_name)
add(10,20)

## OOPS's:

1. class->
   blueprint(plan or structure or design) of an object
   class_name must start with captial letter.
   whenever we create function inside the class we need give,
   def m1(self):
   self is mandatory in class

it contains:
variables and functions

class Class_name:

       self.m3()---->obj1.m3()

2. Inheritance:
   when we want call the previous then it can be done by using "SUPER"
   2.1 single inheritance
   2.2 multi level inheritance
   2.3 hierarchical inheritance
   2.4 Multiple inheritance

3. Polymorphism:
   Method Overriding: two different classes ,single action(function) performing different ways(prints)
   python does not support method overloading
   super()->method overriding

4. Encapsulation:packages

5. Abstraction:

abstract -----> Empty functions
we have to write @abstractmethod above function
if we have abstractmethod make the class as abstract class

## constructor:

to print when the object is created
(we can call when the object is created)

def **init**(self):
print('const')

## Exception:

### predefined exception:

error->an unexpected event that stops the flow of execution of program
complie error->solved by devlopers(syntax error)
logical error->solved by testers
runtime error
if the error and the exception name is not matched then it throws an error

### UDE:

declare exception
create exception
raise exception
handle exception(use try and except)

## Multi

### Thread class:

start--->to strat the thread to run simultaneously
run--->for functions
join()->wait until the thread is terminated

## File Handling:

read :
read-->when we want to read the entire file
readline--->we can read the entire file and can get the particular character by giving the letter in the range
readlines---> can read number of lines in the file in the list form
write:write overrides the existing data in the file(i.e., deletes the previous data)
append:add the given line to the existing file

### Iterators

### MAP----> applies the logic to each and every element

map(function,value)
lambda(arguments:expresion)

### Filter:

filters the data upon given condition

### Reduce

takes the 2 parameters and applies the results to the next parameter

### zip:

it combines the values for given variables
if the values and the variables are not same number then it leaves the values

# PANDAS:

used for data analysis and manipulations or transformation.
pandas->data transformation
numpy
stores in the form of Dataframe
