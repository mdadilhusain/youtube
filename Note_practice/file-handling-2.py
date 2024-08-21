# ### Wap find no of character in a file student.txt

# f = open('student.txt','r')
# data = f.read()
# print(f'Total number of character = {len(data)}')
# f.close()



####WAP find no of lines in a file student.txt

# f = open('student.txt','r')
# data = f.readlines()
# print(f'Total number of line = {len(data)}')
# f.close()



####WAP find no of split in a file student.txt

# f = open('student.txt','r')
# data = f.read()
# data1 = data.split()
# print(data1)
# print(f'Total number of words = {len(data1)}')
# f.close()


####WAP count total vowel and consonants in a file student.txt

f = open('student.txt','r')
data = f.read()
v=c=0
for i in data:
    if i.isalpha():
        if i in 'aeiouAEIOU':
            v+=1
        else:
            c+=1
print(f'Total Vowels = {v}  Total Consonants = {c}')    
f.close()




