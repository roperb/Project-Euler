#Project Euler Problem 3
#
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import array
import math

def genPrimeList(n):
    """returns array of primes below or equal to n"""
    if n < 2:
        return array.array()
    
    primes = array.array('i',[2])
    
    test_number = 3
    while test_number <= n:
        for prime in primes:
            if prime**2 > test_number:
                primes.append(test_number)
                break
            elif test_number % prime == 0:
                break
        test_number += 2

    return primes

def primeFactors(n):
    primes = genPrimeList(int(math.sqrt(n)))
    
    prime_factors = array.array('i')
    
    for prime in primes:
        if n % prime == 0:
            prime_factors.append(prime)
    
    return prime_factors

def main():
    print(primeFactors(600851475143)[-1])
    
if __name__ == "__main__":
    main()
