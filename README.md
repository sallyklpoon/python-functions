# 1510-A2-Functions-functions-functions

## Your name: Sally Poon

## Your student number: A01232177

### *** Any comments you would like me to read before examining your code must go below this line ***

### 1. romannumeral.py
**Decomposition:** This problem has been decomposed into 3 parts, going from the romannumeral function, which considers 
the input number as a whole, checking if there is at thousands digit, then adding that to a second function which 
looks after the input number's digits up to hundreds place. Finally, this second function calls on a third one which
will look at each and every digit and translate it to a roman numeral letter. Decomposition in this module is really
driven by pattern matching.

**Pattern Matching:** With each digit place up to the hundreds in roman numeral (excluding the thousands, which is just 
"M"), there is a particular letter to represent 1 and 5 and a pattern of how special numbers are represented (4, 5, 9). 
This pattern identification allowed me to abstract the problem.

**Abstraction:** Using the recognized patterns, I created GET_ROMANNUMERAL (in blue), which accepts a passed digit as
well as the digit's place value to translate into roman numeral. This function works for place values up to hundreds and
abstracts away from having to create specific if statements for each place value! The abstraction allows this problem to
also be automated.

**Algorithms/Automation:** Since we can simply pass a digit and its place value to GET_ROMANNUMERAL to work, I automated
the process of moving through each digit using HUNDREDS_ROMANNUMERAL (in orange), which will send each digit and its 
place value to the GET_ROMANNUMERAL function until the end and return itself to the ROMANNUMERAL function. Using
automation, the program will loop itself until all digits have been translated properly.

### 2. seconds.py
**Decomposition:** The seconds function has been decomposed into two parts. First, a set-up portion (all in white), 
which defines all the conversion values needed, the format of the conversion, and the output set. Second, the loop 
portion (in purple), which contains an automation to simply convert the total seconds.

**Pattern Matching:** To convert the total_seconds each time, there is a pattern of dividing the total seconds by a
conversion number each time--starting from the largest value all the way to the smallest one. This pattern matching
is the foundation of the automation aspect of this function.

**Abstraction:** In this function, it is not necessary to save the remaining total seconds each time we complete a
conversion, because we will just divide this number by the next conversion. Thus, within the loop, we can update and
re-assign total_seconds each time to the new remainder of total_seconds divided by the last conversion--abstracting away
the need to store the original total_seconds because we will no longer need it as wel convert!

**Algorithms/Automation:** As mentioned above, the pattern that each time we reach a conversion, we will have to divide,
allows a loop to be used to automate the process of iterating through dividing, storing a new total_seconds, and
appending the conversion to the output with each conversion. Through the use of the conversion_list, seconds goes through each conversion and completes the same three
tasks with each conversion until it reaches the end.

### 3. compoundinterest.py
**Decomposition:**

**Pattern Matching:**

**Abstraction:**

**Algorithms/Automation:**

### 4. lottery.py
**Decomposition:**

**Pattern Matching:**

**Abstraction:**

**Algorithms/Automation:**

### 5. phone.py
**Decomposition:**

**Pattern Matching:**

**Abstraction:**

**Algorithms/Automation:**

### 6. leapyears.py
**Decomposition:**

**Pattern Matching:**

**Abstraction:**

**Algorithms/Automation:**

### 7. eratosthenes.py
**Decomposition:**

**Pattern Matching:**

**Abstraction:**

**Algorithms/Automation:**

### 8. moneychanger.py
**Decomposition:**

**Pattern Matching:**

**Abstraction:**

**Algorithms/Automation:**

### 9. dijkstra.py
**Decomposition:**

**Pattern Matching:**

**Abstraction:**

**Algorithms/Automation:**

### 10. caesarcipher.py
**Decomposition:**

**Pattern Matching:**

**Abstraction:**

**Algorithms/Automation:**

### *** Any comments you would like me to read before examining your code must go above this line ***
