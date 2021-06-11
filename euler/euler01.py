#Project Euler Problem 1

def main(maxNumber):
    total = 0
    
    for number in range(maxNumber):
        if number%3==0 or number%5==0:
            total += number
        
    print(total)

if __name__ == "__main__":
    main(maxNumber=1000)




