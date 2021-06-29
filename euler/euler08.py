#Project Euler Problem 8
#Find the largest product of adjacent 13 numbers in the 1000 digit number

def file_to_int_array(filename):
    file = open(filename)
    
    filestring = ""
    int_array = []
    
    for line in file:
        filestring += str(line.strip())

    for i in range(len(filestring)):
        int_array.append(int(filestring[i]))
    
    return int_array


def main():
    int_array = file_to_int_array('euler08.txt')
    
    largest_product = 0
    
    for start in range(0,len(int_array)-13):
        subarray = int_array[start:start+13]
        if subarray.count(0) == 0:
            product = 1
            for num in subarray:
                product *= num
                if product > largest_product:
                    largest_product = product

    print(largest_product)

if __name__ == "__main__":
    main()
    

