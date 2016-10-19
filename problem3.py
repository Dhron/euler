#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#check if a factor of the number given is prime,
#keep track of the largest prime factor

import math

number = 600851475143
maxPrime = 0

def isPrime(n):
    if(n%2==0):
        return False;
    for i in range(2, int(math.sqrt(n))):
        if(n%i == 0):
            return False;    
    return True;

            
for i in range(2, int(math.sqrt(number))):
    if (number%i == 0 and isPrime(i) and i > maxPrime):
        maxPrime = i

print(maxPrime)

