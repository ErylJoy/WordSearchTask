# Word Search Task
- Must be run in python 2 2.7.18 64 bit used for testing as base code was rovided in python2


## Solution 1
Solution 1 is a trivial approach which splits the grid into a list of rows searches each row using the python default operator "in", if found *True* is returned. The list of rows is then transposed and the process is carried out again. If the word is not found by either sections *False* is returned.
O(2n) as there are two passes of the input grid.

## Solution 2
Pretty bad
Somehow worse than the first(Don't really understand that)

## Solution 3
Noice
Linear

O(n) as there is only one pass of the input grid.


## Constraints
only char a-z
 at most 24 characters

## Multicore
Several options for where to apply multi threading since no loops in solutions 1, 2, 3 depend on eachother.
1. Search for each word in a new thread
2. In solution 2 and 3 it is possible to pipe each starting position in the grid to a new thread
3. In solution 1 each row could be searched in a different thread

## Optimisations
Checking final letter in correct place

343.953150034