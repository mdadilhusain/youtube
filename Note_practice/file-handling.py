'''
using method of WRITE function
'''
f=open("student.txt","w")
roll = input("Enter Roll Number ::")
name = input("Enter your full name :: ")
mark = input("Enter marks :: ")
data = roll+"\t"+name+"\t"+mark
f.write(data)
f.close()
print("File Successfully created ...")





f=open("student.txt","w")
while True:
    roll = input("Enter Roll Number ::")
    name = input("Enter your full name :: ")
    mark = input("Enter marks :: ")
    data = roll+"\t"+name+"\t"+mark+"\n"
    f.write(data)
    choice = int(input("1-> Enter More\n2-> Exit\nEnter Your Choice"))
    if choice == 2:
        break
f.close()
print("File Successfully created ...")




# # use of write line function
f = open("data.txt","w")
data = ['1001','raam','99'] #writelines = performce of list of strings
f.writelines(data)
f.close()
print("file created succefully....")


'''
using method of READ function
'''
f = open("student.txt",'r')
data = f.read(20)
print(data)
f.close()





f = open("student.txt",'r')
data = f.read(20)
print(data)
data = f.read(10)
print(data)
f.close()



'''use readline() function'''

f = open('student.txt')
data = f.readline()
print(data)
f.close()



f = open('student.txt')
data = f.readline(5)  # it will read 5 charcters
print(data)
f.close()


f = open('student.txt')
data = f.readline()
print(data,end='')
data = f.readline()
print(data,end='')
f.close()




'''use readline() function'''

f = open('student.txt')
data = f.readlines() #readlines returns list of strings 
print(data)
f.close()


f = open('student.txt')
data = f.readlines() #readlines returns list of strings 
print(data[0])
print(data[1])
f.close()


f = open('student.txt')
data = f.readlines() #readlines returns list of strings 
for i in data:
    print(i,end='')
f.close()
