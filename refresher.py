# Variable names can contain number, letters and underscores. Variable names can't begin with numbers. 

''' Built-in datatypes in python are numbers, strings, boolean, list, tuple and dictionary. Numbers can further be classified into integer, floating numbers and complex
    numbers. Integers and floating point numbers take 4 bytes of memory while bools take 1. If a variable has been assigned a value of some data type. It can be 
    reassigned as a value belonging to some other Data Type in the future.  
    We can use the type() function to know which class a variable or a value belongs to. Similarly, the instance() function is used to check if an object
    belongs to a particular class. 
    One interesting thing to note while working with Python variables is that when we create a variable, we actually create an object somewhere in the memory 
    with a unique mapping or ID/Address. We can see this unique ID generated against each object using id() function.
    
    Python preloads some commonly used values in an area of memory. This memory space has values/literals at defined memory locations and all these locations 
    have different addresses. When we give the command, Age = 20, the variable Age is created as a label pointing to a memory location where 20 is already stored.
    If 20 is not present in any of the memory locations, then 20 is stored in an empty memory location with a unique address and then the Age is made to point to
    that memory location.
    
    Part of the Program where the variable name is legal and accessible is called Scope of the variable. Python has global and local scopes for its variables. '''

    def scope_func():
        name = 'Adarsh Dubey'
        print(name)
    
    scope_func()             # This will print the name
    print(name)              # This will give error as the variable name is defined in local scope ans we are trying to access it from global scope. 
    
    # Lifetime of a global variable is entire program run while lifetime of a local variable is duration of function or the defining block run.
    
    # Typecasting means changing datatypes. Implicit typecast:- When the language typecasts on its own. Explicit:- When done through code written by programmer.
    
    

