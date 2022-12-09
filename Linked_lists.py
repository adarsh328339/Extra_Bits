# Linked Lists are Linear DS used to store the reference to the elements as their own element. 
# Practical Applications consist of implementation of queues, stacks and graphs. Used for folder structure, lifecycle management of OS. 
# Implementing linked lists using collections.deque in Python:- 

from collections import deque
deque()  # Empty linked list created using the collection. Any iterable can be passed using deque and linked list with some elements can be created.

# Passing iterables:- 

deque('abc')
l_list = deque('abc')
# l_list will be equal to deque(['a', 'b', 'c'])
