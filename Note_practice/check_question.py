def swap(num_1,num_2):
    swp = num_1
    num_1 = num_2
    num_2 = swp
    return num_1, num_2
    # print("num_1 = ",num_1,"\nnum_2 = ",num_2)
    
    
    
    
    
    
num_1 = int(input("Enter 1st number :: "))
num_2 = int(input("Enter 2nd number :: "))
a = swap(num_1,num_2)
print("a = ",num_1)


