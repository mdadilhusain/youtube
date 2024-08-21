List = ['adil', 'husain', 234, True, False, 5423,]

print(List,type(List))

print(List[0])
print(List[1])
print(List[2])
print(List[3])
print(List[4])
print(List[5])


print(List[0:5])
print(List[0:6])
print(List[:])
print(List[:len(List)])
print(List[0:])



''' ADD NEW ELEMENTS IN LIST'''

print('===append===')
a = [2,3]  #APPEND method takes only arrgument and add with end

print(a)
a.append("adil")
a.append(1)
a.append(4)
a.append(3)
print(a)

print('===insert===')
a = [4,5,6,7,8,9]

print(a)
a.insert(0,'adil')
a.insert(1,'husain')
print(a)
a.insert(3,'sonu')
print(a)


print('===extend===')
a = [1,2,3]
b = [2,3,4,5]
c = ['a', 'b', 'c']

print(a)
a.extend(b)
print(a)
b.extend(c)
print(b)
c.extend(a)
print(c)

a.append(b)
print(a)

a.insert(1,b)
print(a)


a.extend([5,65,'adil','justice', True,False,4,56.77])

print(a)



a = [1,2,3]
b = [2,3,4,5]
c = ['a', 'b', 'c','d']

a[1] = 54
print(a)
b[3] = 'sonu'
print(b)

print(c)
c[2:3]  = 'rahul',34
print(c)
c[2:4]  = 'rahul',34
print(c)



print('====clear=====')


a = [1,2,3]
b = [2,3,4,5]
c = ['a', 'b', 'c','d']


print(a.clear())
a.append(23)
print(a)
print(a.clear())
a.extend([2,3,4,5,6])
print(a)


print('===remve===')

a = [1,2,3,(2,3,2),4,5]
a.remove(2)
print(a)
# a.remove(89)
a.remove(1)
print(a)

a = [1,2,3,4,5,6,7]
print('===pop===')

a1= a.pop()
print(a)
print(a1)
  

print(a,'\n',a.pop())

a1 = a.pop(1)
print(a)
print(a1)




print('====sort=====')

a = [10,2,73,64,5,66,7]

print(a)
a.sort()
print(a)

print(a)
a.sort(reverse=False)
print(a)

print(a)
a.sort(reverse=True)
print(a)


print("===count====")

a = [1,1,1,2,3,4,4,3,2,1,3]

print(a.count(1))
print(a.count(2))
print(a.count(3))
print(a.count(4))
print(a.count(32)) #0


a = [1.2,3,4.3,5]
b = a.copy()
a.extend([11.2,32,3])
print(a)
print(b)
b.extend([44.55,4,3,453])
print(b)


b = list(a)
a.extend([11.2,32,3])
print(a)
print(b)
b.extend([44.55,4,3,453])
print(b)


print('====index===')

a = [1,2,3,4,5,6,7]


print(a.index(2))

print(a.index(1))

# print(a.index(22))   #ValueError
# print(a.index(5,0,5))
print(a.index(4,3,5))


List1 = ['8' , '3' , '7' , '6' , '5' , '9']
print("returning a sorted list in ascending order : ")
print(sorted(List1))

print("returning a sorted list in descending order : ")
print(sorted(List1,reverse=True))

List1 = ['8' , '3' , '7' , '6' , '5' , '9']

print(List1.count('16'))


