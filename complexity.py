# Big Oh denotes "fewer than or the same as" <expression> iterations.
# Big Omega denotes "more than or the same as" <expression> iterations.
# Big Theta denotes "the same as" <expression> iterations.
# Little Oh denotes "fewer than" <expression> iterations.
# Little Omega denotes "more than" <expression> iterations.

# Big 'Oh Notation eradicates the constants and thus we are only dependent on the variables to calculate the time complexity. 

statement; # This is a constant and thus O(1).

for i in range (N):            # This is a linear time expression. The time taken is directly proportional to the loop. So, a O(N).
    statement;
  
for i in range (N):
    for j in range(N):         # This is a quadratic time expression. Running time is directly proportional to N*N. Thus, a O(N^2)
        statement
        
while ( low <= high ):
    mid = ( low + high ) / 2
if ( target < list[mid] ):     # The running time of the algorithm is proportional to the number of times N can be divided by 2. Thus, a O(logN).
    high = mid - 1
else if ( target > list[mid] ):
    low = mid + 1
else:
    break
    
 def quicksort ( list[], left, right ):
    
    pivot = partition ( list, left, right )
    quicksort ( list, left, pivot - 1 );   # The time consists of N loops (iterative or recursive) that are logarithmic, thus combination of linear and logarithmic.
    quicksort ( list, pivot + 1, right );  # Hence, O(N*logN). 
    
    
# Sequential stuff constitutes addition and nested stuff constitutes multiplication. 
# So two sequential loops would not affect each other in Big-O because they're simplified into the one that has higher growth.
    
for (int i = 0; i < n; i++):
    statement

for i in range n:
    for j in range n:
        statement
 
# These two loops are additive, with the first being O(n) and the second being O(n^2). So you have precisely O(n + n^2). 
# But Big-O removes the lower order parts because the higher order parts totally overwhelm the complexity very quickly,
# and thus the example above has quadratic complexity: O(n^2).
# The second loop has quadratic complexity because the nested loops are defined in terms of each other. 
# You multiply the complexity of the inner loop by the steps of the outer loop to get the total complexity. 
# Since they're both in terms of n, it's a simple matter to say that the two loops combined have quadratic complexity.
    
      
 


