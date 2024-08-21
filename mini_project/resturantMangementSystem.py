#define the menu of resturant
menu = {
    "Pizza": 100,
    "Burger": 40,
    "Pasta": 50,
    "Sausage": 60,
    "Chocolate shake": 70,
    "Dumpling": 80,
    "Coffee" : 20,
}


#greet
print("WELCOME TO PYTHON RESTURANT")
print("===========Dishes==========")
print("Pizza: 100\nBurger: 40\nPasta: 50\nSausage: 60\nChocolate shake: 70\nDumpling: 80\nCoffee : 20")

order_total = 0
item_1 = input("\nEnter the name of item you want to order ::").capitalize()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"\nYour order {item_1} added......")
else:
    print(f"\nOrdered item {item_1} is not avialable yet!")

another_order = input("\nDo you want more item press(Yes) o\w press(No)  :: ").capitalize()
if another_order == "Yes":
    item_2 = input("\nEnter the name of second item :: ").capitalize()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"\nYour order {item_2} added......")
    else:
        print(f"\nYour order {item_2} is not avilable yet!")    
        
print("\n======== Final prize ==========")   
print(f"\nTotal price is  :: {order_total}")
    