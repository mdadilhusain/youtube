# Part 1 -- Calculate the factorial of a given number
# Part 2 -- Find the number of trailing zeros in that factorial  


def factorial(numbers):
    if (numbers == 0 or numbers == 1):
        return 1
    else:
        return numbers * factorial(numbers-1)

def factorialTrailingZeros(numbers):
    count = 0
    i =5
    while (numbers // i != 0):
        count += int(numbers / i)
        i = i*5
    return count    
    
if __name__ == '__main__':
    numbers = int(input("Enter  a number :: "))    
    fac = factorial(numbers)
    print(f"The factorial is {fac}")
    print(factorialTrailingZeros(numbers))