""" STATIC VARIABLES """

# class Staticvar:
#     a = 10     # static variable
#     def disp(self):
#         # print("value of a ="a)     #error
#         print("value of a =",self.a)  # call static variable
#         self.a = 100   # instance variable
#         x.a = 100       # instance variable
#         print("value of a =",Staticvar.a)     #call static variable
        
# print("a =",Staticvar.a)        
# x = Staticvar()
# x.disp()
# print("value of a = " ,x.a) #call instance variable
# print("value of a = " ,Staticvar.a)  #call static variable





class CountObj:
    ctr = 10
    def disp(self):
        print("valie of a =",self.ctr) # call static variable
        
    def accept(self):
        CountObj.ctr = input("Enter a nu:")
        
x =CountObj()
x.disp()        
y = CountObj()
y.disp() 
x.accept()
y.disp()
x.disp() 
print("value of a = " ,CountObj.ctr)