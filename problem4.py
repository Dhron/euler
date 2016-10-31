#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import math


upperLimit = 99801 #largest product of two 3-digit number
lowerLimit = 10000 #smallest product of two 3-digit number

#need to find the largest palindrome number, 
#and then find the two three digit numbers that multiply to get it

def checkPalindrome(number)
{
    numStr = str(number) 
    for i=5, c in numStr:
        if numStr[i] != c
            return;
        else
        i--
}



