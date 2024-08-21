
"""
Accept a number from keyboard , check and display a message whether given number is prime composite or neither prime nor composite .

"""

num = int(input("Enter a number :: "))
flag = False
for i in range(2,num//2):
    if num % i == 0:
        flag = True
        break
    
if num in [0,1,-1]:
    print("Neither prime nor compsite ")    
elif flag:
    print("Composite number ")    
else:
    print("Prime number ")    

