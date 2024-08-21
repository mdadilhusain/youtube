# def show (n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)
    
# show(3)


# def show(n):
#     if n == 0:
#         return
#     else:
#         print(n)
#         show(n-1)
        
        
# show(5)





def fact(n):
    if n == 1:
        return 1
    else:
        k = n*fact(n-1)
    print(k)
    return k 

a = int(input("Enter a number ::"))
print(fact(a))
# print(f"factorial is {fact(a)}")