# Word Search Task
- This must be run in python 2 2.7.18 64 bit used for testing as base code was rovided in python2
- Unit tests on all solutions can be run using the *runUnitTests.sh* script and each solution can be run through with a random selection of words and generated grid using the *tunThroughAll.sh* script. 

## Solution 1
#### Description
Solution 1 is a trivial approach which splits the grid into a list of rows searches each row using the python default operator "in", if found __True__ is returned. The list of rows is then transposed and the process is carried out again. If the word is not found by either sections __False__ is returned.
#### Running
This can be run on a set of randomly selected words and generated a generated puzzle grid by running the test1.py file found in the Test directory.<br />
*cd Tests*<br />
*test1.py*
## Solution 2
#### Description
This solution searches sequentially through the grid, when it matches the first character it then first tries to match the remainder of the word horizontally, failling this is then attempts to do it vertically.  
#### Running
This can be run on a set of randomly selected words and generated a generated puzzle grid by running the test2.py file found in the Test directory.<br />
*cd Tests*<br />
*test2.py*
## Solution 3
#### Description
This solution searches sequentially through the grid, when it matches the first letter it also attempts to match the final letter virtically and horizontally. It will then iterate once through the word and try to match the reamining letters. 
#### Running
This can be run on a set of randomly selected words and generated a generated puzzle grid by running the test3.py file found in the Test directory.<br />
*cd Tests*<br />
*test3.py*
## Solution 4
#### Description
This solutions uses a dictionary which can act as a hash map which uses key value pairs to allow for a very quick lookup speed. It iterates through the grid and places each string of sequential characters into a hash map. Unlike the other solutions which scale in time complexity with the size of the grid and the number of words, this solution only scales in time (and memory) complexity with grid size. This solution however requires vast amounts of memory, for a grid of the size 10,000x10,000 it is only feasable with vast amounts of disposible memory.
As the construction of the hash table can take a long time this solution would eb best in a situation where the searchable data does not change much but different data items may need to be look up within it. For more dynamically changing data solution 3 would be more apt.
#### Running
This can be run on a set of randomly selected words and generated a generated puzzle grid by running the test4.py file found in the Test directory.<br />
*cd Tests*<br />
*test4.py*
## Constraints
Regular expressions are used to verify the input was appropriate, i.e. only lowercase alphabetic strings with no spaces or special characters with a length of nomore than 24 characters.
## Multicore
Several options for where to apply multi threading since no loops in solutions 1, 2, 3 depend on eachother.
1. Search for each word in a new thread
2. In solution 2 and 3 it is possible to pipe each starting position in the grid to a new thread
3. In solution 1 each row could be searched in a different thread

For a system to make use of multiple cores there must be tasks that can be completed independantl. In the task there are several opportunities to take advantage of a multicore system:
1. Each call to __WordSearch.is_present()__ can be called in a different thread as these operations are independant of eachother. This method is implemented in the file *testMultiprocess.py* which can be run with the commands<br />*cd Tests*<br/>*python testMultiprocess.py*
2. In solution 2 and 3 it would be possible to pass each starting position to test to a new thread however this could cause a significant overhead and it therefore may be a better idea to give fewer threads a sectino of the grid to process.
3. In solution 1 parallelsation would be possible by passing each row to be searched to a new thread.
4. In solution 4 multiple threads could be taken advantage of in filling the hash map, however, this cannot be easily implemented in python and would require implementation in a more low level language such as C due to the need of threads to all interact with the same memory space.
## Tests
Unit Tests have been created to test for expected output on given inputs. Implementations of these tests can be found in the files *unitTest1.py*, *unitTest2.py*, *unitTest3.py*, *unitTest4.py*


### testRowOverFlow
Tests that string which would "overflow" a row are not found.

### testOneCharInUniformGrid
Tests that a single charcter string is not able to be found when it is not present.

### testFindsAWordInThePuzzle
Tests that words can actuallly be found in the puzzle by selecting a random word that should be presents and testing for its presence.

### testDoesNotFindNonPresentWords
Tests that random strings that are not present in the grid are not claimed to have been found.

### testRejectsWordsWithCapitals
Tests to make sure the program does not find words containing capital letters.

### testRejectsStringsWithSpaces
Tests that strings containing spaces are rejected.

### testRejectsStringsWithSpecialCharacters
Tests that strings with special characters are rejected.

### testRejectsStringsLongerThan24
Tests that strings longer than 24 characters are rejected.

### testFindsAllProvidedWordsInSearch
Tests that all words that should be present are found.

