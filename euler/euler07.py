#Project Euler Problem 7 - 10001st prime

import array

def gen_prime_list(n):
    """returns array of primes with n elements"""
    if n < 2:
        return array.array('i',[])
    
    primes = array.array('i',[2])
    
    test_number = 3
    while len(primes) < n:
        for prime in primes:
            if prime**2 > test_number:
                primes.append(test_number)
                break
            elif test_number % prime == 0:
                break
        test_number += 2

    return primes

def main():
    n = 10001
    primes_list = gen_prime_list(n)
    print(primes_list[-1])
    
if __name__ == "__main__":
    main()