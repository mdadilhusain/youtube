""" 
Accept a number from keyboard , calculate and display it's reverse .

"""

num = int(input("Enter a number :: "))
rev_num = 0

while num > 0:
    d = num % 10
    rev_num = rev_num * 10 + d
    num = num//10
print(rev_num)
