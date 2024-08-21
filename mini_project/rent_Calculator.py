##input we need from the user 
# Total rent
# Total food ordered for snacking 
# Electricity units spend
# Charge per unit
#persons living in room/hostel

##Output
# # Total amount you have to pay 

rent = int(input("Enter your hostel/flat rent :: "))
food = int(input("Enter the amount of food ordered :: "))
electricity_spend = int(input("Enter your Electricity units spend :: "))
charge_per_unit = int(input("Enter Charge per unit :: "))
persons = int(input("Enter the number of persons living in room :: "))

total_bill = electricity_spend * charge_per_unit

total_amount = (rent+food+total_bill)//persons
print("Each person will pay ::" , total_amount)
