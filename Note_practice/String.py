a =  "A Long Note Book"  
b = 1234567890

print(len(a))
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])
print(a[9])
print(a[10])
print(a[0:14])
print(a[0:])
print(a[0:len(a)])
print(a[0:16])
print(a)
print(a[:])
print(a[:len(a)])
print(a[:2])

a = " adil "
b = "  sonu  "
c = "   sahil   "
d = "    aryan    "


print(len(a))
print(len(b))
print(len(c))
print(len(d))


a1 = a.lstrip()
b1 = b.lstrip()
c1 = c.lstrip()
d1 = d.lstrip()
print(a1,len(a1))
print(b1,len(b1))
print(c1,len(c1))
print(d1,len(d1))

a2 = a.rstrip()
b2 = b.rstrip()
c2 = c.rstrip()
d2 = d.rstrip()
print(a2,len(a2))
print(b2,len(b2))
print(c2,len(c2))
print(d2,len(d2))

f = "  aadil"
print(f.lstrip())

a = "  rohit sharma  "
b = " salman khan "
c = " sharukh khan "

print(len(a))
print(len(b))
print(len(c))
a1 = a.strip()
print(len(a1))
print(b.strip(),len(b))
print(c.strip(),len(c))



a = "rOhIt SharMa"
b = "salMAn kHan"
c = "shArukh khaN"
print("=====capitalize====")
print(a.capitalize())
print(b.capitalize())
print(c.capitalize())


print("=====lower====")

print(a.lower())
print(b.lower())
print(c.lower())

print("=====uper====")

print(a.upper())
print(b.upper())
print(c.upper())


print("====center(len)")

print(a.center(len(a)+8,'-'))
print(b.center(len(b)+8,'!'))
print(c.center(len(c)+8,'^'))

print("====count=====")

print(a.count('p'))
print(b.count('a'))
print(c.count('q'))  

print('====endstwith=====')

print(a.endswith("."))
print(b.endswith('n'))
print(c.endswith('N'))


print('====index====')


print(a.index('a'))
print(b.index('Ha'))
print(c.index('h'))
# print(a.index('x'))    # value Error


print('====Difference between find or index====')


a = 'rays patna'
print("===find==")
print(a.find('p'))
print(a.find('x'))   # -1
print(a.find("g"))   # -1
print(a.find('s'))
print(a.find('t'))


print('===index===')

print(a.index('p'))
print(a.index('s'))
print(a.index('t'))  
# print(a.index('x'))  # ValueError
# print(a.index("g"))  # ValueError



a = 'rays'
b = "123"
c = "RAYS45"
d = 'rays4543'
e = 'adil1-234 Adil'

print("===isalnun===")
print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print(d.isalnum())
print(e.isalnum()) # FALSE because if you use isalnum so make sure don't use any space or any symbol 


a = 'adil'
b = 'ADIL'
c = 'AdilHusain'
d = 'Adil Husain'
e = 'adil123'         


print('===isalpha===')
print(a.isalpha())
print(b.isalpha())
print(c.isalpha())    
print(d.isalpha())  #FALSE
print(e.isalpha())  #FALSE


a1= 'adil'
a = "😂😂😂😂😂😂😂😂😂❌❌✔️✔️✔️✔️✖️✖️✖️✔️❎✅🆚🆚🆚🆚💮"
b1 = "2.5"
b = '5'
c = " "

print('====isalpha====')

print(a1.isascii())
print(a.isascii())
print(b1.isascii())
print(b.isascii())
print(c.isascii())

print('====isprintable===')

print(a1.isprintable())
print(a.isprintable())
print(b1.isprintable())
print(b.isprintable())
print(c.isprintable())

print('===isspace===')

print(a.isspace())
print(a1.isspace())
print(b1.isspace())
print(b.isspace())
print(c.isspace())







