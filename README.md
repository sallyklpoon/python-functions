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
the need to store the original total_seconds because we will no longer need it after each iteration of converting!

**Algorithms/Automation:** As mentioned above, each time we reach a conversion divide the previous value of
 total seconds by the current conversion. I've used a loop to automate the process of iterating through dividing, 
storing a new total_seconds, and appending the conversion to the output with each conversion. 
Through the use of the conversion_list, seconds goes through each conversion and completes the same three
tasks with each conversion until it reaches the end.

### 3. compoundinterest.py
**Decomposition:** Compound interest can be decomposed based on the order of operations. First, get 2 operands (in blue)
, which can happen simultaneously, then bring operand1 to the power of operand2. Finally, the last step is to multiply
that result by the principal.

**Pattern Matching:** Since parenthesis and exponents are the first to be executed in PEDMAS, I recognized that
these two processes must go first before the final multiplication.

**Abstraction:** This function will calculate accrued amount of money with the given parameters. Being a program
that is written based on a formula--this is a form of abstraction! A formula is a fact or rule written to apply to the
general process of finding the value of something, so it is in a sense a form of abstraction.

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

**Abstraction:** There is no need to create a new helper function to randomly select numbers.
In this module, I blindly trust that the black box of SAMPLE() will, undoubtedly, return 6 unique, random numbers 
within a given range. Using this helper function, we can easily change the length of the list we want, and the range
by modifying the parameters passed to SAMPLE().

**Algorithms/Automation:** In my 'guess' of the black box in random SAMPLE(), there is a process of automation where a
number will continue to be drawn until we reach the end of the specified k number of elements we want. In addition to
that, since we've already asked SAMPLE() to draw 6 elements from the range of [1, 49], the LOTTERY() function literally
does not need any parameters to be passed as arguments. Calling LOTTERY() by itself will provide an appropriate result.

### 5. phone.py
**Decomposition:** Phone has been decomposed to use one other helper function that leads to two smaller, 'sub-functions'
, if you will. First off the function phone itself will append translated characters to a new string for 
translated_phone. If the character isn't a "-" character, then we will ask ALPHA_TO_NUMBER to get a translation result
to append to the translated_phone number. To keep the functions short, this helper function will then send the
alphanumeric character off to the right path for mapping translation. The 'sub-functions' (MAP_2TO5 and MAP_6TO9)
performs the task of mapping to the character to the correct number.

**Pattern Matching:** Each alphanumeric character in the list will need to be looked at and will require the use of the 
exact same steps for translation. Thus, I've used a for-loop to go through each character and have each of them be 
evaluated using one shared process. 

**Abstraction:** Instead of typing out each and every character for the numbers, I abstracted by use of declaring the
mapped letters within each number right away. This helps not only with legibility, but also because ALPHA_TO_NUMBER()
will check which list a character belongs to, I will not have to re-write each and every character tediously. Declaring
the mapped letters up top also can permit other users importing to use these variables which are generally the mapped
letters to numbers on all phone numbers!

**Algorithms/Automation:** As mentioned in pattern matching, because each character in a phone number (other than 
 the '-') needs to be looked at, I automated the process of 'flipping' through each number until the end of the string
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
range of years has been automated by indirection to this helper function. It is not necessary in our code to use
multiple if/else statements to calculate which years are leap years.

### 7. eratosthenes.py
**Decomposition:** This function can be broken down into 3 parts. An assigning and setup portion (in white), a large
for-loop (in blue) that may have values to use in a nested for loop (in yellow).

**Pattern Matching:** Using Eratosthenes method, we check each number to ask if it is a prime number. Starting from
2 until the square root of the upper bound, we go through the original list, cross off numbers that are not
the current evaluating number and are divisible by the current evaluating number until we reach the end of the original
number list we are working with. We then repeat this step with the next number in the evaluating list all the way until
we reach the end of evaluating numbers list.

**Abstraction:** Eratosthenes' method to get prime numbers within a range of numbers works and is applicable to any
range of numbers. Thus, this function, based on the method, can also apply to any range of positive numbers.

**Algorithms/Automation:** The process of comparing each number in an original list with an evaluating number has been 
automated. This is great because we do not need to generate a unique list of evaluating numbers each time we have a
different upper bound passed. Instead, the evaluating list is automatically created, and we will flip through each
evaluating number after we've checked, removed, and exhausted the original number list we are working from.

### 8. moneychanger.py
**Decomposition:** This module is broken into two separate functions. The first of which is the main, MONEYCHANGER()
function, which does the work of compiling the output list, and the second is ROUNDOFF_PENNIES() function which does the
job of rounding off pennies in order for the MONEYCHANGER() function to work smoothly without any snags.

**Pattern Matching:** To calculate the least amount of change necessary, we have to work with from largest to smallest 
numbers. Just like seconds conversion, any type of conversion will require the need to divide an original amount by a 
conversion amount. This is shared across all the different currency values. In some ways, we can think of it as the 
total_dollar amount needs to be passed from one conversion to the other, doing the same task of being division and 
appending to an output list. The orange for-loop has been created to do exactly that as it goes down the list of 
Canadian currency values.

**Abstraction:** Aside from the fact that the MONEYCHANGE() function being able to be applied to any amount of money, I 
used abstraction when it came down to rounding off pennies. Instead of having the program evaluate each 0.01, 0.02...
0.10 decimal ending for total_dollars, I asked my program to look only at the hundredths decimal number--because this is
all you need to determine whether to round up/down to the closest 5 or 0 cents. Note also that we only need to check 3 
different cases:
1. if the hundredths is '.', in which case, the total_dollar amount has a 0 decimal that Python has gotten rid of
2. if the hundredths is in the range of 1 to 2, in which we round down to closest 0
3. if the hundredths is in the range of 3 to 7, in which we round to 5 cents

If it's none of the above cases, we assume we must round up to closest 10 cents!

**Algorithms/Automation:** By use of pattern matching, I identified that we will have to roll through every conversion 
using total_dollars. I've automated this process by use of the orange loop, which will pass and update the total_dollars
amount down the list of different conversion values. The program will automatically end once total_dollars has been 
passed through all the items in the canadian_currency list. 

### 9. dijkstra.py
**Decomposition:** The DIJKSTRA() function can be broken into three different parts. First, there is a process of
counting the number of each colour there is and creating a string of these tallied colours. The second part is forming
a list out of these elements through the helpful split method to turn strings quickly into a list. Finally, the third 
portion is a loop to move each of the elements in this new formed tally list to the original list which has been 
cleared (in orange).

**Pattern Matching:** Since we are grouping colours all together, we can simply count and write however many times each
colour appears in the original list. Tally it up by writing the colour x number of times (x being the total count).
Finally, we just need to slide these elements into the original passed list, and we are good ot go.

**Abstraction:** This function will work for any number of elements in a list containing "red", "white", and "blue".
It isn't important that we pop and move the elements in the original list around (which could end up being more work 
and more prone to errors). Instead, using abstract and creative thinking, I chose to create a temporary new list 
quickly and easily by counting and adding these elements into the original list.

**Algorithms/Automation:** The process of appending all the elements in the tally list to the original list has been
 automated so that any length of list can adapt easily in the program. Using this for-loop (in orange), we do not need 
to monitor when we stop appending elements because the loop will exit once we reach the end of the tally list.

### 10. caesarcipher.py
**Decomposition:** This module is broken up into one main function which uses a helper function to do a smaller task.
First, the main CAESARCIPHER() function will accept all the necessary values, then evaluate encode Boolean to determine 
if we need to modify the shift (not submitted shift if encode is false) before sending it to the cipher_character 
translator. The CIPHER_CHARACTER() is the second part. It will convert each of the characters based on the shift passed
from CAESARCIPHER().

**Pattern Matching:** Both encoding and decrypting is the same process. We need to look at each character and shift a 
given number of values; however, one is applying the shift and one is taking away the shift. This pattern allows us to 
use a similar loop between encoding and decrypt as seen in the blue and purple loop (they resemble each other). It also
 encourages us to use abstraction.

**Abstraction:** Since both encoding and decrypting have a similar process, I used one helper function only, which does 
ciphering by accepting the corrected shift from the CAESARCIPHER() function and using it to determine the 
character's converted character. We do not need a specific function for each encoding and decrypting.

**Algorithms/Automation:** The caesar cipher will require us to translate each and every character. A for-loop is 
extremely helpful in automating the process of passing each character to CIPHER_CHARACTER(). Using these loops, the 
program will automatically end and return the result once all characters in the string has been looked at.

### *** Any comments you would like me to read before examining your code must go above this line ***
