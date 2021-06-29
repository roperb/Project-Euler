#Project Euler Problem 5



def generate_factor_list(n):
    factor_list = []
    for i in range(1,n//2+1):
        if n%i == 0:
            factor_list.append(i)

def main():    
    n = 20

    factor = 2
    while True:
        if n % factor != 0:
            n += 20
            factor = 2
        elif factor == 20:
            print(n)
            break
        else:
            factor += 1

if __name__ == "__main__":
    main()
    