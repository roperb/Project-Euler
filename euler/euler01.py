#Project Euler Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.


def main(max_number=1000):
    total = 0
    
    for number in range(max_number):
        if number%3==0 or number%5==0:
            total += number
        
    print(total)

if __name__ == "__main__":
    main()




