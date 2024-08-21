# a = {1,2,3,4,5,6,7,8,9,0}

# for b in a :
#     print(b)
    
    
    
# c = ['ram' , 'shyam' , 'rohan' , 'sohan' , 'raju'] 

# for d in c :
#     print(d)
    
    
    
# a = [2,3,4,5,6,76]
# i = 0
# while i<len(a):
#     print(a[i])
#     i+=1
    
# a = [2,3,4,5,6,76]
# for b in a:
#     print(b)    
    
    
# txt = "Rays Education PVT LTD 2019"    

# for i in txt:
#     print(i)

    
# txt_1 = "Rays Education PVT LTD 2020"    
# i = 0
# while i < len(txt_1):
#     print(txt_1[i])
#     i+=1

# n = int(input("Enter N number :: "))
# for i in range(1,n+1):
#     print(i)

# for a in range (5):
#     print(a)


# for a in range (1,11):
#     print(a) 


# for i in range (1,11,1):
    # print(i)

# for a in range(211,0,-12):
#     print(a)
    
# import time as t

# i = 10
# while i >=0:
#     print(i)
#     t.sleep(0.1)
#     i-=1
    
    
# for i in range(10,-1,-1):
#     print(i)
#     t.sleep(0.1)

# a = 0 ; b = 1 
# num = int(input("Enter a number :: "))
# print("Fibonanci series ", a , b ,end=' ' )
# for t in range(num-2):
#     c = a+b
#     a = b
#     b = c
#     print(c,end=' ')
    


##Fibonanci series

# a = 0 ; b = 1
# num = int(input("Enter many number\'s Fibonanci series you want :: "))        
# print("Fibonanci series" , a ,b ,end=' ')
# for t in range(num-2):
#     c = a+b
#     a = b
#     b = c
#     print(c,end=' ')


# n = int(input("Enter a no :: "))
# flag = False
# for d in range(2,n//2+1):
#     if n%d==0:
#         flag = True
#         break
# if n==1:
#     print("Neither prime nor composite")
# elif flag:
#     print("composite")    
# else:
#     print("prime")


# #(1) Counting positive Number 
# number = [1, -2, -3, 4, 5, 6, -7, -8, 9, -10]
# pov = 0
# i = 0
# while i < len(number):
#     if number[i]>=i:
#         pov+=1
#     else:
#         pass
#     i+=1
# print("Total positive no : ",pov)


# number = [1, -2, -3, 4, 5, 6, 0, -7, -8, 9, -10]
# pov = 0
# for i in number:
#     if i>=0:
#         pov+=1
#     else:
#         pass    
# print("Total number of ::",pov)    


# #(2) sum of Even number
# n = int(input("Enter N number :: "))
# sum_even = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         sum_even+=1
#     else:
#         pass
# print("final result of total even :: ",sum_even)        


# #(3) Multiplication Table printer
# no = int(input("Enter a no:: "))
# for i in range(1,11):
#     if i == 5 :
#         continue
#     m = no*i
#     print(no,'X',i,'=',m)

# #(4) Reversed a string
# input_str = "Python"
# reversed_str = ''
# for char in input_str:
#     print(char)
#     reversed_str = char + reversed_str 
# print(reversed_str)    

# #(5) Find the First non-repeated character
# input_str = input("Enter a string : ")    

# for char in input_str:
#     print(char)
#     if input_str.count(char) == 1:
#         print("char is ",char)
#         break


# #(6) Factorial calculator
# number = int(input("Enter a number :: "))
# factorial = 1

# while number > 0:
#     factorial*=number
#     number-=1
# print("Factorial number value of :: ",factorial)    


# #(7) validation input 
# while True:
#     number = int(input("Enter a number b/w 1 to 10 :: "))
#     if 1 <= number <=10:
#         print('Thanks for input correct digit ')
#         break
#     else:
#         print("Invalid number , try again ")



##(8) Prime number checker
# number = int(input("Enter a number :: "))
# is_prime = True
# if number > 1:
#  for i in range(2,number):
#     if number%i==0:
#         is_prime = False   
#         break
# if is_prime is True:
#     print("Given no is prime ::",number)
# else:
#     print("Given no is not prime",number)




##(9) List uniqueness checker
# '''Problem :: Check if all elements in a list are unique . if a diplicate is found,exit the loop and print the duplicate'''
# items = ["apple", "banana", "orange", "apple", "mango", "lemon"]

# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("Duplicate : ",item)
#         break
#     unique_item.add(item)
    
    

# ##(10) Exponential backoff    
# '''Problem :: implememt an exponential backoff strategy that doubles the wait time between retries , starting from 1 second , but stops after 5 retries'''

# import time as t

# wait_time = 1
# max_retries = 5 
# attempts = 0

# while attempts < max_retries:  
#     print("Attempt",attempts + 1, "_wait time ", wait_time)
#     t.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1
    