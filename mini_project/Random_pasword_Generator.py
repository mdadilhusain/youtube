import random
import string


pass_len = 8
charValues = string.ascii_letters + string.digits + string.punctuation

"""with list comprehension [function for i in range(n)] """
password = "".join([random.choice(charValues) for i in range(pass_len)])
""" with for loop """
# password = ''
# for i in range(pass_len):
#     password += random.choice(charValues)
    
print(f"Your password is : {password}") 
