# Learning more OOP. Today subclasses

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    

class Student(Person):  # Subclass
    def __init__(self, name, age, student_id, course_id):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__course_id = course_id

    def get_student_id(self):
        return self.__student_id
    
    def get_course_id(self):
        return self.__course_id
    

class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject):
        super().__init__(name, age)
        self.__teacher_id = teacher_id
        self.__subject = subject

    def get_teacher_id(self):
        return self.__teacher_id
    
    def get_subject_id(self):
        return self.__subject

        

def main():
    p1 = Person("PersonTest", 23)
    print(p1.get_name())

    s1 = Student("StudentTest", 2, 100, 1)
    print(s1.get_name())

    t1 = Teacher("TeacherTest", 99, 500, "Computer Science")
    print(t1.get_name())

if __name__ == "__main__":
    main()