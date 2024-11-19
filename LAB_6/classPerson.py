class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person1 = person("alice",25)
person2 = person("Bob",30)

print(f"person 1 name: details - {person1.name}, age = {person1.age}")
print(f"person 2 name : details - {person2.name}, age = {person2.age}")