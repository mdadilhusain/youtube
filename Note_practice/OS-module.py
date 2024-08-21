import os 
import datetime as d
# print(os.getcwd())
# os.mkdir('india')
# os.chdir('india')
# print(os.getcwd())
# print("india")
# os.makedirs('bihar\\sivan')
# print(os.listdir())
# os.removedirs('bihar\\sivan')


# print(os.getcwd())
# if os.path.isdir('patna\\diwan'):
#     print('yes')
# else :
#     os.makedirs('patna\\diwan')   
# print("code successfully run...")


# import os 
# print(os.getcwd())
# if not os.path.isdir('india\\patna'):
#     os.makedirs('india\\patna')
# os.chdir('india\\patna')
# f = open('info.txt','a')
# f.write(input("Enter Your sentece :: "))
# f.close()
# print("program successfully run....")



# f = open('student.txt')
# print(f.read(5))
# print(f.tell())
# f = open('india\\patna\\info.txt',"a")
# print(f.tell())



# f = open("student.txt",'a')
# print(f.tell())
# print(f.seek(20))



# # # # append mode 
# import os 
# if not os.path.isdir("india\\patna"):
#     os.makedirs("india\\patna")
# os.chdir('india\\patna')    
# f = open('info.txt','a')
# print(f.tell())
# f.write(input("enter a sentence :: "))
# print(f.tell())
# f.close()



# # # # write mode

# import os 
# fol = input("Enter a directory name :::")
# if not os.path.isdir(fol):
#     os.makedirs(fol)
#     print('dir created successfully......')
# os.chdir(fol)
# file = input("enter a file name .txt ::")
# f = open(file,'w')
# print("Current curser position ",f.tell())
# f.write(input("Enter a sentence ::"))
# print('Now curser position is  ',f.tell())
# f.close()
# print("Work done......")





# import os
# fol = input("Enter a directory name :::")
# if not os.path.isdir(fol):
#     os.makedirs(fol)
#     print('dir created successfully......')
# os.chdir(fol)
# file = input("enter a file name .txt ::")
# f = open(file,'a')
# print("Current curser position ",f.tell())
# f.write(input("Enter a sentence ::"))
# print('Now curser position is  ',f.tell())
# f = open(file,'r')
# print(f.tell())
# f.seek(6)
# print(f.tell())
# print(f.read(6))
# f.close()
# print("Work done......")


###making a year ,month and day wise folder -------->>>>>>>


# cdate = d.datetime.now()
# mdir = cdate.strftime('%Y')+'/'+cdate.strftime('%b')+'/'+cdate.strftime('%a')
# if not(os.path.isdir(mdir)):
#     os.makedirs(mdir)
#     print("Directory is successfully created.....")
# else :
#     print("Directory is already exists")    