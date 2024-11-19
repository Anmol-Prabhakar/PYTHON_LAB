class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

student1 = student("john",19)
student2 = student("sam",20)

print(f"student 1: Name - {student1.name}, age - {student1.age}")
print(f"student 2: Name - {student2.name}, age - {student2.age}")