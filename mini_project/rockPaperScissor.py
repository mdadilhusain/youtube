import random
"""  
1 rock 
-1 paper
0 scissor
"""
computer = random.choice([1,0,-1])
userStr = input("Enter your choice (rock , paper , scissor) :: ")
var_dict = {'rock' : 1 , 'paper' : -1 , 'scissor' : 0}
rev_var_dict = {1 : 'Rock' , -1 : 'Paper' , 0 : 'Scissor'}
user = var_dict[userStr]

print(f"Your choice is {rev_var_dict[user]}\nComputer choice is {rev_var_dict[computer]}")

if (computer == user):
    print("It's draw")
else:
    if (computer == 1 and user == -1):
        print(f"{rev_var_dict[user]} covers {rev_var_dict[computer]}---> you win!")
    elif (computer == 1 and user == 0):
        print(f"{rev_var_dict[computer]} smashes {rev_var_dict[user]}---> you lose!")
    elif (computer == -1 and user == 1):
        print(f"{rev_var_dict[computer]} covers {rev_var_dict[user]}---> you lose!")
    elif (computer == -1 and user == 0):
        print(f"{rev_var_dict[user]} cuts {rev_var_dict[computer]}---> you win!")
    elif (computer == 0 and user == 1):
        print(f"{rev_var_dict[user]} smashes {rev_var_dict[computer]}---> you win!")
    elif (computer == 0 and user == -1):
        print(f"{rev_var_dict[computer]} cuts {rev_var_dict[user]}---> you lose!")
    else:
        print("somthing wrong!")    
