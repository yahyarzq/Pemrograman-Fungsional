class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


studentList = []
studentList.append(Student("Alex", 20))
studentList.append(Student("Bob", 21))
studentList.append(Student("Ira", 15))


print(studentList)
for student in studentList:
    print('Name : {}, Age : {}'.format(student.name,student.age))