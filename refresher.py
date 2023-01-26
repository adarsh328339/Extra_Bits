# Variables and Datatypes

''' Variable names can contain number, letters and underscores. Variable names can't begin with numbers. 

    Built-in datatypes in python are numbers, strings, boolean, list, tuple and dictionary. Numbers can further be classified into integer, floating numbers and complex
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
    
    ''' Lifetime of a global variable is entire program run while lifetime of a local variable is duration of function or the defining block run. '''
    
    ''' Typecasting means changing datatypes. Implicit typecast:- When the language typecasts on its own. Explicit:- When done through code written by programmer. '''
    
    # Basic I/O in Python
    
    ''' Syntax of print() is print(object(s), sep = seperator, end=end, file=file, flush=flush). Since print() ends with a default newline character, so to end it with
        some other character we use end param. Sep param is udes to define the seperator between different values to be printed. Sep = Space by default. '''
    
    x, y = input().split()              #This will take multiple input in a single line and store them in the respective variables. 
    
    
    # Operators in Python
    
    a ** b     ''' This denotes a raised to the power b. Identity Operators like is and is not are also used in python to check for same objects. '''
    list1 = [11,2,33]
    list2 = [11,22,33]
    print(list1 is list2) ''' Gives False as output because lists are immutable. 
    Python also has membership operators like in and not in to check for membership of a specific value in an object. Bitwise operators act on bits. ^ is bitwise XOR.
    Left Shift by 1 multiplies the number by 2. Right Shift by 1 divides by 2. << is left shift. Exponent operates right-to-left in python.
    PEDMAS is the precedence of operators. D=M and A=S. '''
    
    0.1 + 0.2 == 0.3        ''' Gives false as neither of these can be represented accurately in binary. Thus, some differences. '''
    
    
    # Loops and other stuff:-
    
    range(start,stop,step)    ''' This is the range function iterating from start to stop-1 with step steps.
    While Loop is used to iterate as long as the consition is true. Can be used when the condition is unknown. 
    
    
    
    
    
    
    
    

