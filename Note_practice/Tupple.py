a = ()
print(a,type(a))


a = (1)
print(a,type(a))  # this not tuple a single item tuple always sperated with a coma make sure

a = (1,)
print(a,type(a))

a = (1,2,3,43,23,2,43,3,2,4,2)
print(a,type(a))

for i in a:
    print(i)

i = 0
while i < len(a):
    print(a[i])
    i+=1
    
    
a = (True,1,2,3,4,'adil', 'sahil', 'ahil', 'farhan', 'aman')    

i = 0
while i < len(a):
    print(a[i])
    i+=1


a = (True,1,2,3,4,'adil', (1,'adil',2,3,2,4,),'sahil', 'ahil', 'farhan', 'aman')      

print(a[1:])
print(a[3])
print(a[:])
print(a[0:])
print(a[-1])
print(a)
a = (True,1,2,3,4,'adil', (1,'adil',2,("monu",'sonu',(123,34)),2,4,),'sahil', 'ahil', 'farhan', 'aman')    
print(a)  
print(a[6])
print(a[6][1])
print(a[6][1][1])
print(a[6][3][2][1])


# a[0] = 1 #TypeError


b = a # same 


# a.clear()   # AttributeError
print(a)

if a is b:
    print('same')
else:
    print('duplicate')    
    
    
a = (22,323,14,1,432,3)
d = input("Enter super admin or admin")
if d == "super admin" or d == '11' :
    print("welcome back super admin ")
    a = list(a)
    a.extend([1,2,3,4,5,6,76]) 
    a = tuple(a)
    print(tuple(a),type(a))
else:
    a = tuple(a)    
    print(a)
    print('u re not super admin')




a = (22,3,8,8,323,14,14,1,432,3)

print(a.count(1111),type(a))


print(a.count(22))
print(a.count(8))
print(a.count(14))
print(a.count(3))


print(a.index(8,2,-2))
# print(a.index(18)) #ValueError 
print(a.index(14))





''' (1) Accept N numbers from keyboard delete and display it's elements in LIFO fashion '''

num = int(input("How many number"))
v = []
for i in range(num):
    v.append(input("Enter a num :: "))
print(v)    
print("year elements are in LIFO fashion : ")    
while len(v) > 0:
    print(v.pop(),end=',')