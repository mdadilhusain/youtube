"""WAP Keep adding a stream of numbers inputted by the user . The adding stops as soon as user presses q key on the keyboard. """

total_Amount = 0

while True:
    user_Input = input("Enter a amount or quit(q) :: ")
    if (user_Input.upper() == 'Q'):
        print("Thank you using our calculator")
        break
    user_Input = int(user_Input)
    total_Amount += user_Input
    
    
print(f"Your total amount is : {total_Amount}")    