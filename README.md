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
**Decomposition:** Compound interest can be decomposed based on the order of operations. First, get 2 operands (in blue)
, which can happen simultaneously, then bring operand1 to the power of operand2. Finally, the last step is to multiply
that result by the principal.

**Pattern Matching:** Since parenthesis are and exponents are the first to be executed in PEDMAS, I recognized that
these two processes must go first before the final multiplication.

**Abstraction:** This function will calculate accrued amount of money after with the given parameters. Being a program
that is written based on a formula--this is a form of abstraction! Formulas is a fact or rule written to apply to the
general process of finding the value of something.

**Algorithms/Automation:** This function prevents the need to manually calculate by hand using PEDMAS, it has been
structured to automate the process of calculating compound interest. Because of it being based off a formula, we can
automate the process of calculating compoundinterest for varying amounts that fit within the preconditions.

### 4. lottery.py
**Decomposition:** This function is decomposed into two parts. One part is a helper function called SAMPLE() imported 
from the random library. This function will produce 6 random and unique numbers. The second part of this function is
the main function, which will take the result of SAMPLE() and return it sorted.

**Pattern Matching:** Since we must have number that is within [1, 49], my computational thinking around the SAMPLE()
function will draw from the same range of [1, 49] each time without replacement and each time the number
is drawn, it will be added to the result list, and we will have to decrease the number of objects we need by 1. These
steps contribute to the automation of the function.

**Abstraction:** There is no need to create a specific function to random sample, but trusting that the black box of
SAMPLE() will, undoubtedly, return 6 unique, random numbers within a given range. Using this helper function, we can
easily change the length of the list we want and the range.

**Algorithms/Automation:** In my 'guess' of the black box in random SAMPLE(), there is a process of automation where a
number will continue to be drawn until we reach the end of the specified k number of elements we want. In addition to
that, since we've already asked SAMPLE() to draw 6 elements from the range of [1, 49], the LOTTERY() function literally
does not need any parameters to be passed as arguments. Calling LOTTERY() by itself will provide an appropriate result.

### 5. phone.py
**Decomposition:** Phone has been decomposed to use one other helper function that leads to two smaller, 'sub-functions'
, if you will. First off the function phone itself will append translated characters to a new string for 
translated_phone. If the character isn't a "-" character, then we will ask ALPHA_TO_NUMBER to get a translation result
to append to the translated_phone number. To keep the functions short, this helper function will then send the
alphanumeric character off to the right path for mapping translation. The 'sub-functions' the character will be mapped.

**Pattern Matching:** Each alphanumeric character in the list will need to be looked at and will require the use of the 
exact same steps for translation. Thus, I've used a for-loop to go through each character and have each of them be 
evaluated using one shared process. 

**Abstraction:** Instead of typing out each and every character for the numbers, I abstracted by use of declaring the
mapped letters within each number right away. This helps not only with legibility, but also because ALPHA_TO_NUMBER()
will check which list a character belongs to, I will not have to re-write each and every character tediously. Declaring
the mapped letters up top also can permit other users importing to use these variables which are generally the mapped
letters to numbers on all phone numbers!

**Algorithms/Automation:** As mentioned in pattern matching, because each character in a phone number (other than 
 the '-') needs to be looked at, I automated the process of flipping through each number until the end of the string
using a for-loop in PHONE() (in purple).

### 6. leapyears.py
**Decomposition:** This module has been broken down into a main function, LEAPYEARS() and a helper function imported
from calendar LEAPDAYS(). LEAPDAYS() is a function that will find leap years within a given range, we simply need to
send the correct lower_bound and upper_bound (+ 1 to make sure upper_bound is included) to that function.

**Pattern Matching:** Since there is a regular pattern to finding leap years (year is divisible by 4, 100, and 400),
any range of years as long as lower bound is less than or equal to upper bound, will be able to use this same LEAPDAYS()
pattern to determine if it is a leap year.

**Abstraction:** This function can be generalized to any lower and upper bound years as long as lower bound is less
than or equal to upper bound.

**Algorithms/Automation:** Since LEAPYEARS() is used, the process of algorithms to find leap years within a given
range of years has been automated by indirection to this helper function. It is not necessary in our code to use diff

### 7. eratosthenes.py
**Decomposition:** This function can be broken down into 3 parts. An assigning and setup portion (in white), a large
for-loop (in blue) that may have values to use in a nested for loop (in yellow).

**Pattern Matching:** Using Eratosthenes method, we check each number to ask if it is a prime number. Starting from
2 until the square root of the upper bound, we go through the original list, cross off numbers that are not
the current evaluating number and are divisible by the current evaluating number until we reach the end of the original
number list we are working with. We then repeat this step with the next number in the evaluating list all the way until
we reach the end of evaluating numbers list.

**Abstraction:** Eratosthenes' method to get prime numbers within a range of numbers works and is applicable to any
range of numbers. This function, too, based on the method, can apply to any range of numbers.

**Algorithms/Automation:** The process of comparing each number in an original list with an evaluating number has been 
automated. This is great because we do not need to generate a unique list of evaluating numbers each time we have a
different upper bound passed. Instead, the evaluating list is automatically created and we will flip through each
evaluating number after we've checked, removed, and exhausted the original number list we are working from.

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
