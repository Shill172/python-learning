# Learning more OOP. Today subclasses

class Person:
    def __init__(self, name, age, num_classes=5):   # 5 Classes deafult
        self.__name = name
        self.__age = age
        self.__num_classes = num_classes

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_num_classes(self):
        return self.__num_classes
    

class Student(Person):  # Subclass
    def __init__(self, name, age, student_id, course_id, num_classes=5):
        super().__init__(name, age, num_classes)
        self.__student_id = student_id
        self.__course_id = course_id

    def get_student_id(self):
        return self.__student_id
    
    def get_course_id(self):
        return self.__course_id
    
    def get_num_classes(self):  # Overriding
        return self.__num_classes
    
    def change_num_classes(self):
        try:
            self.__num_classes = int(input("How much classes do you want to take? "))
        except ValueError:
            print(f"Give an int. Not {type(self.__num_classes)}.")
            self.__num_classes = 5

    def __str__(self):
        return f"Student name: {self.get_name()}, ID: {self.__student_id}"
    

class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject, num_classes=5):
        super().__init__(name, age, num_classes)
        self.__teacher_id = teacher_id
        self.__subject = subject

    def get_teacher_id(self):
        return self.__teacher_id
    
    def get_subject_id(self):
        return self.__subject

    def get_num_classes(self):  # Overriding
        return self.__num_classes
    
    def __str__(self):
        return f"Teacher name: {self.get_name()}, ID: {self.__teacher_id}"
    


        

def main():
    p1 = Person("PersonTest", 23)
    print(p1.get_name())

    s1 = Student("StudentTest", 2, 100, 1)
    print(s1.get_name())

    t1 = Teacher("TeacherTest", 99, 500, "Computer Science")
    print(t1.get_name())

    print(s1)

    print(t1)

    s1.change_num_classes()

    print(s1.get_num_classes())

    people = [p1, s1, t1]
    for person in people:
        print(person.get_num_classes())


if __name__ == "__main__":
    main()