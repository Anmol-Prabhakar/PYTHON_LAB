class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

student1 = student("John",2)

print(f"student 1 details: name - {student1.name} , rollno - {student1.rollno}")
