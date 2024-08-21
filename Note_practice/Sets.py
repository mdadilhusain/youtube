a  = {}
a1  = {'rays'}
a2  = {'rays' , 'rays' , 'rays' , 'adil'}
a3 = {'rays' , 'soft' , 'apple' , 'orange' , 'soft'}

print(a,type(a),len(a))
print(a1,type(a1),len(a1))
print(a2,type(a2),len(a2))
print(a3,type(a3),len(a3))

'''
print(a3[0]) #set object is not subscriptable
print(a3[1:4])  # Error
'''


'''
a[0] = 'adil'  #TypeError: 'set' object does not support item assignment
a2[2] = '6'    #TypeError: 'set' object does not support item assignment
'''


print('====add====')
#add single value 

a = {1, 3, 'rays', 4, 1, 'adil', 65}
a.add('adilhusain')
print(a)

# a.add('rohit', 999, 'abhisekh')  # TypeError: set.add() takes exactly one argument (3 given)

b = a.add('9999')
print(b)   # None return
print(a)

c = a.add('rukshana khatoon ')
print(c)  # None return
print(a)

print('====update====')
#Add multiple value

a = {'rays' , 'soft' , 'apple' , 'orange' , 'soft'}

# a.update('2' , '5' , 'aryan' , 'Flase')
# print(a)

b = a.update({'husain' , 4 , 'Alam'})
print(b)  #None
print(a)

c = a.update({'rohit' , 'ajay' , 'iterable' , 'song'})
print(c)  #None
print(a)

print("====clear====")
#Fully empty set

a = {'rays' , 'soft' , 'apple' , 'orange' , 'soft'}
a.clear()
print(a)  #set()


b = a.clear()
print(b)   #None
print(a)   #set()



print("===del===")
#delete entire set

a = {'rays' , 'soft' , 'apple' , 'orange' , 'soft'}

del a
# print(a)  #NameError: name 'a' is not defined


print("====Remove=====")
# if given value is not exisit in set in that case code raise Error
a = {'rana' , 'pana' , 'orange' , 23}

a.remove('rana')
print(a)

# a.remove('adil')
# print(a)  #KeyError: 'adil'

b = a.remove(23)
print(b)  #None
print(a)

print("====discard====")

a = {'rana' , 'pana' , 'orange' , 23 , 45 , 'sohan' , 'aditiya' , 'samma' , 'shabina' , 'Farhan'}
print(a)
a.discard("rana")
print(a)

a.discard("samma")
print(a)
 
a.discard("adilhusain") #if given argument not in set so not raise error print set as usual as before
print(a)


b = a.discard('shabina')
print(b)  # None
print(a)



print("====pop====")

a = {'rana' , 'pana' , 'orange' , 23 , 45 , 'sohan' , 'aditiya' , 'samma' , 'shabina' , 'Farhan'}

b = a.pop()
print(a)
print(b)

b = a.pop()
print(a)
print(b)


print("=====union=====")

x = {'a' , 'b' , 'd'}
y = {'b' , 'c' , 'e'}
a = {'a' , 'f' , 'g'}

z = x.union(y,a)
print(x)
print(y)
print(a)
print(z)

x = {'a' , 'b' , 'd' ,9}
y = {'b' , 'c' , 'e' ,5 , 7}


z = x.union(y)
print(x)
print(y)
print(z)



print("====intersection=====")

x = {'a' , 'b' , 'd'}
y = {'b' , 'c' , 'e'}

z = x.intersection(y)
print(x)
print(y)
print(z)


x = {'adil' , 'sohan' , 'rishav' , 'ajay'}
y = {'adil' , 'ajay' , 'rishav' , 'stiya'}

z = x.intersection(y)
print(x)
print(y)
print(z)



print("====difference=====")


x = {'a' , 'b' , 'd'}
y = {'b' , 'c' , 'e'}
g = {'c' , 'd' , 'k'}

z = x.difference(y,g)
print(x)
print(y)
print(g)
print(z)

z = x.difference(y)
print(x)
print(y)
print(z)


print("====difference_update====")

x = {'a' , 'b' , 'd'}
y = {'b' , 'c' , 'e'}

r = x.difference_update(y)
print(r)
print(x)
print(y)


print("=====intersection_update======")


x = {'a' , 'b' , 'd'}
y = {'b' , 'c' , 'e'}

r = x.intersection_update(y)
print(r)
print(x)
print(y)



print("======symetric_difference====")

x = {'a' , 'b' , 'd'}
y = {'b' , 'c' , 'e'}

r = x.symmetric_difference(y)
print(r)
print(x)
print(y)



print("======symetric_difference_update======")

x = {'a' , 'b' , 'd'}
y = {'b' , 'c' , 'e'}

r = x.symmetric_difference_update(y)
print(r)
print(x)
print(y)




cities = {'tokyo' , 'madrid' , 'seoul'}
cities2 = {'tokyo' , 'seoul' , 'kabul' , 'madrid'}

cities1 = {'tokyo' , 'madrid3' , 'berlin'}
cities3 = {'tokyo' , 'seoul' , 'kabul' , 'madrid'}

cities4 = {'tokyo' , 'madrid' , 'berlin' ,'delhi'}
cities5 = {'seoul' , 'kabul'}

a = {1,2,3,4,5}
b = {5,3,4,2,1}


print("=======isdisjointset=====")

print(cities.isdisjoint(cities2))
print(cities1.isdisjoint(cities3))
print(cities4.isdisjoint(cities5))
print(a.isdisjoint(b))




print("=====issuperset=======")

print(cities.issuperset(cities2))
print(cities1.issuperset(cities3))
print(cities4.issuperset(cities5))
print(a.issuperset(b))



print("======issubset========")

print(cities.issubset(cities2))
print(cities1.issubset(cities3))
print(cities4.issubset(cities5))
print(a.issubset(b))




print("======duplicate of set")
x = {1,2,3,4,5}
y = x
x.add('adil')
print(x)   #same
print(y)    #same

if x is y:
    print('same')
else:
    print('duplicate')    


print("====set dupplicate methods====")


a = {1,2,3,4}
y = a.copy()

if a is y:
    print("same")
else:
    print("dupplicate")    



a1 = {1,2,3,4,44,54}
y1 = set(a1)   
if y1 is a1:
    print('same')
else:
    print("dupplicate")    