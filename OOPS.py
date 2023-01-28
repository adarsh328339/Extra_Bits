#OOPS and the terminology around it

''' OOPS makes Development and Maintenance of a project more easier for the developer. Data can be hiddden or managed more efficiently and thus promoting 
    security prospects. '''

''' Objects :- Anything that has state and some behaviour associated with it. Integers, strings, floats, arrays, and dictionaries, are all objects. 
    Class:- A class is ablueprint (a plan basically) that is used to define (bind together) a set of variables and methods (Characteristics) that are
    common to all objects of a particular kind. Classes are used to create user-defined data structures. Classes define functions called methods ,
    which identify the behaviors and actions that an object created from the class can perform with its data. ''' 



# Creating a new Class named Employee:- 
Class Employee:
    def __init__(self, post, name):        # Constructor function is used to instantiate an object and assign variables. Always called during object creation
        self.post = post
        self.name = name                   # Self is a reference to the current instance of the class. Used to access the attributes and methods in the class

emp1 = Employee('Manager', 'Rahul')        # A new object is created and parameters are passed. 


# Encapsulation in OOPS:- 

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
        
    def display(self):
        print('The basic details about the employee are as follows:', self.name, self.salary)
        
    def work(self):
        print('The work details of the employee are as follows:', self.name, self.department)
        
emp2 = Employee('Rohit','Technical', 8000)
emp2.display()
emp2.work()


#Inheritance in Python :- 

''' Inheritance can be defined as the process through which one class can use the properties, fields and methods of another class. The class inheriting the 
    properties is called Subclass and the class from which the properties are inherited is called Base or Parent or Superclass. '''

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Male(Human):
    
        



        


        
  
