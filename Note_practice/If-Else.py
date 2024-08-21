_a = int(input("Enter a no : "))
b = int(input("Enter b no : "))
c = int(input("Enter c no : "))

if a > b and a > c :
    print("Height no: ", a )
elif b > a and b > c :
    print("Height no : ", b)    
else:
    print("Height no : ", c)    



a = int(input("Enter a no : "))
b = int(input("Enter b no : "))
c = int(input("Enter c no : "))

if a>b:
    if a>c:
        print("Height no : ", a )
    else:
        print("Height no : ", c)    
elif b>c:
    print("Height no : ",b)        
else:
    print("Height no : ",c)    




a = int(input("Enter a no : "))
b = int(input("Enter b no : "))
c = int(input("Enter c no : "))
d = int(input("Enter d no : "))

if a>b:
    if a>c:
        if a>d:
            print("Height no : ",a)
        else:
            print("Height no : ",d)    
    elif c>d:
        print("Height no : ",c)        
    else:
        print("Height no : ",d) 

elif b>c:
    if b>d:
        print("Height no : ",b)           
    else:
        print("Height no : ",d)    

elif c>d:
    print("Height no : ",c)
else:
    print("Height no : ",d)    
    
    
    
    
    
a = int(input("Enter a no : "))
b = int(input("Enter b no : "))
c = int(input("Enter c no : "))    
    
if a>b:
    if b>c:
        print("Middle no : ",b)
    elif a>c:
        print("Middle no : ",c)
    else:
        print("Middle no : ",a)    
elif a>c:
    print("Middle no : ",a)        
elif b>c:
    print("Middle no : ",c)    
else:
    print("Middle no : ",b)    





year = int(input("Enter a year : "))

if year%100==0 and year%400==0:
    print(" Leap Year ")
elif year%100!=0 and year%4==0:
    print(" Leap Year ")    
else:
    print(" Not Leap Year ")    

    
    
    
year = int(input("Enter a no : "))

if year%100==0:
    if year%400==0:
        print(" Leap Year ")    
    else:
        print(" Not Leap Year ")    
elif year%4==0:
    print(" Leap Year ")        
else:
    print(" Not Leap Year")    