class Student:
    numberOfStudent = 0
    schoolName = "HMPS"

    def __init__(self ,name, rollNumber , marks):
        self.name = name
        self.rollNumber = rollNumber
        self.marks = marks
        self.numberOfStudent = Student.numberOfStudent + 1
        
    def study(self):
        print("I am "+ str(self.rollNumber) +"and i am studying")    
        
    def play(self):
        print("pdh liya , now i am going to kehlene")    
        
        
        
        
print(Student("adil husain",1,48))
s2 = Student("rahil", 2, 47)
