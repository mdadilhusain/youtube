""" Write a program to enter the number of products , then product name, quantity and price and create a list of tuples .At last Display the Bill and Total Bill """


number_of_products = int(input("Number of products  :: "))
products = []
total_bill = 0

#taking Input Through User
for i in range(1,number_of_products+1):
    print(f"{"="*10}PRODUCT NUMBER{i}{"="*10}")
    product_name = input("Product Name  :: ")
    product_quantity = float(input("Product Quantity  :: "))
    product_price = float(input("Product Price  :: "))
    products.append((product_name,product_quantity,product_price))


#display Item

print("\n\nWELCOME TO ADIL SUPERMART\n\n")
print("NAME\tQUANTITY\tPRICE\tTOTAL")

for item in products:
    total = item[2]*item[1]
    #formating
    print(item[0],'\t',item[1],'\t\t',item[2],'\t',total)
    #totalBill
    total_bill +=(item[2]*item[1])
    
 
print("\n\nTOTAL BILL = ",total_bill)
print("Thanks for shopping........")

    
    
                   