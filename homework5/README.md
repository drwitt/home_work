# Homework \#5
*python data types, conda environments, control flow*  


## Problem 0
Create your personal branch in this repo via github (i.e. you don't need the command line
tools to do this). Give it whatever name you like. **Now, Fork this repo!!**. `git clone`
your fork to your local machine. Complete the rest of these exercises on your machine.

## Problem 1 - `conda env`ironment
- Create a new conda environment named `hmw5` and use python 3.5 (I know 3.7 is latest).
- Install `jupyter` in this environment.


## Problem 2 - `Closed Laptop`
In other words, try to do these without the aid of your broswer or `docstrings`.
1. Provide the expected output, if error, put "error".  
    a. len({1, 1, 1.0, 1j, 'hello'}) 3  
    b. len((1, 1, 1.0, 1j, 'hello')) 5 
    c. len([1, 1, 1.0, 1j, 'hello']) 5 
    d. z = {1, 4.0, 'no'}; z[0]  error
    e. z = (1, 4.0, 'no'); z[0] = 9  z=(9,4.0,'no')
    f. z = [1, 4.0, 'no']; z[0] = 9  z=[9,4.0,'no']
    g. (e) demonstrates what property of tuples?  It is a set of unordered collection of items within that evevy elements is unique with no duplication and immutable. 
    h. (f) demonstrates what property of lists?  List is collection of ordered and changeable items which allows duplicate elements. 
    
## Problem 3
Using the conda environment from `Problem 1`, start a jupyter client-server application. Use
this application to create a notebook named `homework5`. Within this notebook:
1. Print all available magics available.  
2. Demonstrate understanding of **`line magics`** by using one to print the current working directory.  
3. Demonstrate understanding of **`cell magics`** by using one to print the current working directory.  
4. Create a list with the elements 'whiskey', 'tango', 'foxtrot' and call it names.  
5. Create a tuple with the elements 'happy', 'eager', 'sad' and call it adjectives.  
6. Use a `for` loop (or multiple for loops) to create all possible adjective-noun combinations (e.g. 'sad-tango').  
7. Using a new cell, copy code from 6. Modify the copy of the loop so that `sad-tango` is never printed.  
8. Using a new cell, copy code from 6. Modify the copy of the loop so that `happy-foxtrot` triggers the looping to stop.  

## Problem 4
1. Export your environment to a .yml file.

## Problem 5
1. Make sure all materials (i.e. updates to this README, juypter notebook, .yml file) are all
within the `home_work` repo in the homework 5 folder.
2. Complete the local git workflow to get the your answers in a commit.
3. git push these changes to **your fork**, you can choose the branch.
4. From your fork, submit a pull request that **puts these changes in your branch** in the bios821-2018 organization.
