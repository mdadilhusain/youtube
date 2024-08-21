# """create a class with two attributes -balance and account no . create methods for debit ,credit and printing the blacnce.""" 

""" making CLass """
# class Check_Balance:
#     def __init__(self , acc_no , bal):
#         self.acc_no = acc_no
#         self.bal = bal
#         print("Account No ::",acc_no,"\nCurrent balance : " ,bal )
#     #method for debit
#     def debit(self , amount):
#         self.bal -= amount
#         print("Rs ", amount,"was debited")
#         print("total balance", self.get_bal())
        
#     #method for credit
#     def credit(self, amount):
#         self.bal += amount
#         print("Rs ", amount,"was credit")
#         print("total balance", self.get_bal())
#     # check current balance
#     def get_bal(self):
#         return self.bal
    
""" making objects """
# acc1 = Check_Balance(101, 123456)    
# acc1.debit(20000)
# acc1.credit(1020)
        
        
        
        
        
# print(50*"="+'parctice questionn'+50*"=")        


""" making CLass """
# class Distance:
#     feet=inch=None
#     def input(self, a , b):
#         self.feet = a
#         self.inch = b
#     def disp(self):
#         print("feet = ", self.feet,"inch = ",self.inch)    

""" making objects """
# x = Distance()
# x.disp()
# x.input(10,20)
# x.disp()




# """ Exceptional case whithout self formal parameters """

""" making CLass """
# class Check:
#     def disp():
#         print("display called")
#     def high(a,b):
#         if a > b: return print("highest no is ",a)
#         else : return print("highest no is",b )   

""" making objects """
# y = Check
# y.disp()
# y.high(12,45)








""" making CLass """
# class Convert:
#     feet=inch=0
#     def check(self):
#         if self.inch >= 12:
#             self.feet += self.inch//12
#             self.inch = self.inch%12
#         print("Feet = ",self.feet,",Inch = ",self.inch)  
#     def disp(self , a , b):
#         self.feet = a 
#         self.inch = b      


""" making objects """
# show = Convert()
# show.disp(13,18)
# show.check()
# show.disp(14,8)
# show.check()








