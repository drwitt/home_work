# Homework #6
Please complete all questions below in a conda environment hosting your own jupyter interactive computing environment.
**Do not push any of your homework to github until Thursday's class. If you post homework early, I will take 20 points 
off.**

1. A Caesar cipher is a very simple method of encoding and decoding data. The cipher simply replaces characters 
with the character offset by k places. For example, if the offset is 3, we replace `a` with `d`, `b` with `e` etc. The 
cipher wraps around so we replace `y` with `b`, `z` with `c` and so on. Punctuation, spaces and numbers are 
left unchanged. In order to complete this assignment, look into the python package `string`, it may be helpful.

(a) Write a function named `encode` that takes as arguments a string and an integer offset and returns the encoded
cipher. Be sure to document your function.

(b) Write a function named `decode` that takes as arguments a cipher and an integer offset and returns the decoded
string.

(c) Write a function named `letter_count` that takes as argument a string and returns a tuple. The first element in the 
tuple is a dictionary. The dictionary's keys are comprised of every unique upper case letter from the english alphabet. 
The values in this dictionary are percentages of the times that letter (either lower or upper case) is present in the 
input string.  The second element in the tuple is the number of letters either upper or lower case in the input string.

(d) Use the following nursery rhyme to test all three functions above and use a random offset between 5 and 9 
where needed:
```
Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall;
All the king's horses and all the king's men
Couldn't put Humpty together again.
```