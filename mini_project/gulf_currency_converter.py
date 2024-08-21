with open('C:\\Users\\mdadi\\OneDrive\\PYTHON-FILE\\mini_project\\currency.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parse = line.split("\t")
    currencyDict[parse[0]] = parse[2]
    
amount = int(input("Enter amount :: "))

print("List of the currency names ")

[print(item) for item in currencyDict.keys()]

currencyName = input("Enter currency name :: ")

print(f"{amount} {currencyName} is equal to {amount * float(currencyDict[currencyName])} INR")






     