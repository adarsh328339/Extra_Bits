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



        


        
  
