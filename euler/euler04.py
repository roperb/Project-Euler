#A palindromic number reads the same both ways.
#Find the largest palindrome made from the product of two 3-digit numbers.

#import sys
#sys.path.insert(0, '/Users/brianroper/Documents/github/math')
#sys.path.insert(0, '/Users/brianroper/Documents/github/genLibrary')
#
#from checkIfPalindrome import checkIfPalindrome

def is_palindrome(n):
    n = str(n)
    n_inverse = ""
    for i in range(len(n)):
        n_inverse += n[len(n)-1-i]
    
    return n == n_inverse

def main():
    lowerBound = 900
    upperBound = 1001

    largestPal = 0
    for i in range(lowerBound,upperBound):
        for j in range(lowerBound,upperBound):
            if is_palindrome(i*j) and i*j > largestPal:
                largestPal = i*j

    print(largestPal)
    
if __name__ == "__main__":
    main()

