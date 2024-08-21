# # local variable
# # Global variable
# a = 20   #global variable
# def disp():
#     b = 10  #local variable
#     print(f"a = {a}    b = {b}")
# c = 30  # global variable
# def show():
#     print(f"value of a = {a}")
#     # print(f"value of b = {b}")   #NameError: name 'b' is not defined
#     print(f"value of c = {c}")
# print(a)    
# # print(b) #NameError: name 'b' is not defined
# print(c)
    
    
    
# disp()   
# show()
# print(a)
# # print(b)  #NameError: name 'b' is not defined
# print(c)
    
    
    
    
    
    
# ''' Shadowing process'''

# a = 10
# def disp():
#     a = 20
#     print(f"value of a = {a}")
    
    
# disp()    
# print(f'value of a = {a}')



# # Global Method

# a = 10 
# def disp():
#     global a
#     a = 20
#     print(f"value of a - {a}")
# def move():
#     print(f'value of a is {a}')
# disp()
# print(f"value of {a}")
# move()


