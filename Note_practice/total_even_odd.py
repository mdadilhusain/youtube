"""
Accept N number from keyboard count and display total even and odd numbers.

"""
n = int(input("Enter N NUMBER :: "))
odd = 0 ; even = 0

for i in range(1,n+1):
    if (i % 2 != 0) or (i in [0]):
           odd += 1 
    else :
        even += 1
print(f'totla even {even} and total odd {odd}')        
               