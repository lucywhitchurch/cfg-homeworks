# My Theory Assignment

## 1. How does Object Oriented Programming differ from Process Oriented Programming?
OOP divides the program into small parts called objects, whereas POP divides the program into small parts called functions. OOP allows for code reusability, POP does not. OOP takes a bottom up approach, whereas POP takes a top-down approach. In OOP, it is easy to add new data and functions whereas in POP it is not. OOP gives the option to use specifiers (like private, public, protected), whereas POP does not. OOP uses the data abstraction whereas POP uses procedure abstraction. OOP also gives the option of data hiding and inheritance, POP does not. The option of data hiding in OOP means it is more secure and POP is less secure. OOP is used for designing large programs, POP is better suited for designing medium-sized programs. OOP is used in languages such as C++, Java, Python, C#, POP is used in languages such as C, FORTRAN, Pascal, Basic.

## 2. What's polymorphism in OOP?

Polymorphism is the condition where an occurrence appears in many different forms. In programming, this refers to a single object, operator or method being used for many different types. This can therefore have many different uses and perform various different tasks. For this to happen, the child class(es) inherits all the methods and attributes from the parent class. 

An example of polymorphism with in-built functions:
~~~python

print(len("code first girls"))

print(len(["banana", "apple", "pear"]))
~~~
This demonstrates how some functions in python are polymorphic, which means they are able to act on multiple different data types. Len() is used to return the length of an object and will measure and return the result dependent on the data type referenced. So for a string it will return the number of the characters, whereas for a list it will return the number of items.

## 3. What's inheritance in OOP?
In polymorphism, a class acts as a blueprint and an object acts as a concrete instantiation of the blueprint. Each class will contain methods, which are passed to the objects which instantiate that class. When a child class is created, it inherits all the methods and attributes from this parent class. However, sometimes not all the methods are useful to child class and so they can be reimplemented in the child class. The redefine pre-existing methods in the child class, we use method overriding.
An example of inheritance and method overriding:

~~~python
class Person:

  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def introduce(self):
    print(f"My name is {self.firstname} {self.lastname}")


class Student(Person):
  def __init__(self, firstname, lastname, course):
    super().__init__(firstname, lastname)
    self.course = course

  def hello(self):
    print(f"Hi, I'm {self.firstname} {self.lastname}, I'm studying {self.course}")

x = Student("Lucy", "Whitchurch", "Software development")
print(x)
~~~

Here, Person is the parent class, containing firstname, lastname and age attributes with an introduce method. Student is the child class, passing the Person parent class through its parameters, therefore inheriting its attributes and methods. The __init__() function creates the new object and overrides the inheritance of the parents function, meaning methods can be reimplemented. Here, the course method was added. The super()__init__ function inherits all the other methods and attributes from the parent class. New methods can be added, like the hello function.

## 4.	If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people?


•	Create a voting system SQL database with a table containing employee details, such as: employee id, name, date of birth, department

•   Connect SQL database to python project using a flask framework

•	Create file containing a sign up system function for employees who want to vote, checking their details with the employee sql table and pushing to a separate table in the database which contains participants details

•	The sign up form will ask participants their name, employee, id, department and dob and then ask them to create a new username and password

•	Create a login function, taking in username and password and allowing the user through if they match the details in the database. Only allowing the user 3 attempts at entering details until they are locked out

•	Once the user is through, display a list of candidates and a number next to them

•	Ask user to input the number of the candidate they want to vote for, save their vote, push it to a separate table in the database called votes, containing names of candidates and number of votes

•	Pull from the votes table to display candidate with highest number of votes once everyone has had chance to cast their vote

•	Link this with html and css templates for user interface and styling


## 5. What's the software development cycle?

The software development life cycle (SDLC) is a framework which lays out the task during each consecutive stage of the software development process. This methodology aims to cover all bases to maximise the teams efficiency and ensure a high quality product is delivered. It is important to note that some project managers may adapt this cycle dependant on their own personal approach, so some steps may be broken down, combined together, omitted or repeated. The 7 main stages are:
1.	Planning – project managers work alongside stakeholders to identify the goals for the project, working out priorities and developing a timeline. They also calculate the costs and labour figures.
2.	Define requirements – considered an extension of the planning process. This stage is carried out to create a clear plan for the requirements of the project and to manage the expectations of all parties.
3.	Design – this stage sets out a basic idea of how the product looks as works and sometimes uses prototypes to bring this to life and to get feedback on.
4.	Building – also called the software development stage. This may be completed by an individual or team. During this stage, they will work to write the code for the program, as well as fix bugs along the way.
5.	Testing – testing may be automated or manual. Tests are created and carried out to ensure the program functions as expected and runs smoothly. Testing decreases the chances of bugs and lagging and results in higher customer satisfaction.
6.	Deployment – the program is rolled out and made available to the users. This may be automated or not. It also could be a simple or complex process, depending on the scale of the project and amount of other interfering programs.
7.	Operations and maintenance – This is the final stage of the SDLC. After the program has been rolled out to the users, operations and maintenance monitors the program to identify and bugs or glitches which need to be fixed. This also helps in highlighting issues for future development plans and new releases.

## 6. What's the difference between agile and waterfall?

Agile in a non-linear process which involves a continuous cycle through a number of development and testing stages, it follows an incremental approach methodology.
Waterfall, on the other hand, is a linear model, which follows a sequential methodology. This means that agile allows for a flexible approach to the software development process as it allows for changes in approach throughout the development stages. As waterfall provides a more structured methodology, it is rigid in its approach and does not allow for changes in requirements throughout the development process. Agile divides the project into a lifecycle of sprints, so evolves into a collection of smaller projects. Waterfall divides the project into a series of distinct phases, so the software development process is completed in a singular project. Taking an iterative approach, means the while using agile, the software development process may cycle through a number of planning, development and testing stages more than once, whereas when using waterfall, each step will appear only once. As such, in agile methodology, testing is performed concurrently throughout the development phases of the project, and in waterfall, it comes at a singular specified point in the process which is following the build phase. Agile has a product mindset and offers flexible change as per the customers requirements, whereas waterfall takes a project mindset and focuses on the fulfilling original customer proposal. This is shown in the team setup, as in agile, no project managers are required as the team is self-sufficient and managed internally by themselves. However, waterfall requires a project manager to oversee each stage of the project.

## 7. What is a reduced function used for?

This function in python allows you to reduce a list in a concise way. The reduced(fun,seq) applies the function passed in its arguments to the list items in the given sequence also in its arguments. It works by first taking the first two elements of a sequence and applying the function to give a result. It then works from left to right and applies the same function to the next element in the list using this result, and so on. The process continues until all the elements in the sequence are reduced into a single value, which is stored and printed to the console. To use reduce(), it needs to be imported from the functools module. To make the code more precise and readable, the reduced function is regularly used with lambda functions, for example:
~~~python
from functools import reduce

myList = [1, 2, 3, 4, 5]


result = reduce( (lambda x,y: x*y), myList)
print(result)
~~~
Here the function is carry out: 1 x 1 = 1. 1 x 2 = 2. 2 x 3 = 6. 6 x 4 = 24. 24 x 5 = 120.

## 8. How does merge sort work?
Merge sort is the most significant divide-and-conquer sorting algorithms. The divide part is carried out first as the algorithms begins by roughly dividing the initial unsorted array in half. If there are an odd number of elements, one half is larger by one element. The subarrays are then continuously divided in half until each sublist contains only one element each. Next the conquer part begins. The single-element sublists are repeatedly merged into two-element sub-lists, sorting it in the process. This again, is repeated to merge the sublists into four-element arrays and so on, until you are left with a singular sorted array. This process is recursive as the algorithm repeatedly calls itself until the array is divided and conquered and only then does the recursion halt.
[!For example:] (lucywhitchurch/documents/screenshot.png")

## 9. Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is the use case?
Generators allow us to implement iterators in a more elegant and concise way. They achieve the same results as iterators but are used without the __iter__ and __next__ and StopIteration methods/principles in a class. Instead, the yield keyword is used in place of the normal return keyword. Yield has extended functionality and is able to remember the state of a function so the next time it is called, it can continue the process without starting from the beginning. The result of this ‘lazy’, on demand generation is improved performance and lower memory usage, so are considered to be a more succinct way of creating iterators.
For example:
~~~python
def gen():
    n = 2
    print('First even number')
    yield n

    n += 2
    print('Second even number')
    yield n

    n += 2
    print('Third even number')
    yield n


g = gen()
print(next(g))
print(next(g))
print(next(g))
~~~
In this example, the gen function is defined normally, but with the absence of a return statement and presence of the yield statement means it runs as a generator. The generator runs through the function without saving everything to the memory, instead it assigns the variable without resolving it. As it reaches each yield statement, this acts as a breakpoint in the code, temporarily pausing the operation of the iteration and maintaining the result until the next yield keyword is called again.

## 10. Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator?

A decorator (or metaprogramming) is a function which is used to modify a function or class in python to enhance its functionality and return a new, different version of it. It does this by calling a higher function and applying it to the latter function, thereby altering the behaviour of the original function/class, without changing it in its entirety. Decorators are typically stored in their own separate module to ensure the code is clear. They can also be called repeatedly using the @ symbol so are reusable in python. Furthermore, multiple decorators can be chained, meaning a function can be decorated with various different decorators at the same time. 
For example:
~~~python
def exclamation(func):
    def inner(*args, **kwargs):
        print("!" * 10)
        func(*args, **kwargs)
        print("!" * 10)
    return inner


def wave(func):
    def inner(*args, **kwargs):
        print("~" * 10)
        func(*args, **kwargs)
        print("~" * 10)
    return inner


@exclamation
@wave
def hello(msg):
    print(msg)

hello("Hello Emily/Ali/Shepstone, how are you? Are you bored marking this assignment?")
~~~