with open('C:\\Users\\mdadi\\OneDrive\\PYTHON-FILE\\mini_project\\currency.txt') as f:
    lines = f.readlines()
    
currentDict = {}
for line in lines:
    parsed = line.split('\t')
    currentDict[parsed[0]] = parsed[1]
    
# Enter the indian currency     
amount = int(input("Enter amount ::\n "))

# currency Options
print("\n\nEnter the name of the currency you want to convert this amount to? Available Options :\n\n".upper())

# currency name print using list comprehension
# [print(item) for item in currentDict.keys()]

# currency name print using loops
for item in currentDict.keys():      # | using loop
    print(item)                      # | 
    
# convert currency name 
currency = input("\n\nplese enter one of these values : \n\n")


print(f" {amount} INR is equal to {amount*float(currentDict[currency])} {currency}")