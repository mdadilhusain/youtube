a = {2 : 'adil' , 4 : 'micro' , 43 : 'soft' , 6 : 'mango' , 65 : 'micro'}
print(a)
print(a[4])
print(a[2])
# print(a[44])  #KeyError: 44
a = {4 :19 ,3 :2 , 4 : 16}
print(a)

print("====get====")

print(a.get(45))
print(a.get(6))
print(a.get(65))

print(a,type(a),len(a))

print(a.keys(),type(a))
print(a.values(),type(a))
print(a.items())
a.update({3:'rohit',9:"mohit"})
print(a)

a1 = a.pop(4)
print(a)
print(a1)



a1 = a.popitem()
print(a1)
a1 = a.popitem()
print(a1)
print(a.popitem())

a.clear()
print(a)



b = a.copy()
if a is b:
    print('same')
else:
    print('dupplicate')    
    
    
b = dict(a)
if a is b:
    print('same')
else:
    print('dupplicate')    
    