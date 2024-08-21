def disp():
    print("disp method called")

    
    
def check(a):
    if a % 2 == 0:
        print("Given no ",a,"is even ")    
    else:
        print("Given no ",a,  "is odd")    

def high(a,b):
    if a > b:
        return a
    else:
        return b 
    
    
disp()
check(2)
high(4,8)    
disp()
check(5)
high(6,2)

print("=====positional argument=====")

def vote(name,age):
    print(f'my name is {name} i am {age} year old ')

vote('adil', 18)
vote(18, "adil")
# vote('adil')   #TypeError: vote() missing 1 required positional argument: 'age'
# vote()   #TypeError: vote() missing 2 required positional arguments: 'name' and 'age'


print("========Keyword argument======")

def vote(name = "adil" , age = 20):
    print(f'my name is {name} and i am {age}')
    
vote('sonu',56)    
vote()
vote("aman")
vote(45)



print("=====default argument====")

def vote(name,age = 56):
    print(f'my name is {name} and i am {age}')

vote('adol',20)
vote('adil')
vote()



def vote(name = 'adil',age):
    print(f'my name is {name} and i am {age}')
    
# vote(45)    #SyntaxError: parameter without a default follows parameter with a default


print("=====arbitray arguments=====")

def fruits(*e):
    print(e,type(e))
    
fruits()    
fruits('apple')
fruits("banana","apple")
fruits("grapes","pineapple","lemon","watermilion")


def fruit(*p):
    if len(p) == 0:
        print("Arguments must be passed ")
    else:
        for a in p:
            print(a)    
            
fruit()            
fruit("grapes","pineapple","lemon","watermilion")



