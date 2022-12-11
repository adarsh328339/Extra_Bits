# Linked Lists are Linear DS used to store the reference to the elements as their own element. 
# Practical Applications consist of implementation of queues, stacks and graphs. Used for folder structure, lifecycle management of OS. 
# Implementing linked lists using collections.deque in Python:- 

from collections import deque
deque()  # Empty linked list created using the collection. Any iterable can be passed using deque and linked list with some elements can be created.

# Passing iterables:- 

deque('abc')
l_list = deque('abc')

# l_list will be equal to deque(['a', 'b', 'c'])

# Performance Comparision of a List and Linked List :-

l1.remove() and l1.insert() # These are O(n) operations. Not meant for .remove() last element as its equivalent to .pop() 
l1.pop() and l1.append() # These are O(1) operations

# Insertion and Deletion of elements :- 
# If inserting or removing the element at beginning, linked list are better and offer O(1) solution.
# If inserting the element at the end or removing from end, Both linked list and lists behave similarly. 




# Implementing queues (FIFO) using deque And some methods associated with queues:- 

from collections import deque 
queue = deque()
queue.append('Adarsh')
queue.append('Dubey')
queue.popleft('Adarsh') 

# Implementing stacks (LIFO) using deque and some methods associated with it :- 
from  collections import deque

history = deque()
history.appendleft('Web1')
history.appendleft('Web2')

history.popleft()





