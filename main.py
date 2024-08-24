class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = []
    def add_grade (self, grade):
        if 0 <= grade <=100:
            self.grades.append(grade)


    def get_average_grade (self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def __str__(self):
        average = self.get_average_grade()
        return f"Name: {self.name}, Grades: {self.grades}, Average: {average}"



class Classroom:
    def __init__(self):
        self.students =[]
    def add_student (self, student):
        self.students.append(student)

    def get_top_students(self):
        sorted_students = sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)
        return sorted_students[:3]
    def get_failed_students (self):
        failed_students = []
        for student in self.students:
         if student.get_average_grade() < 51:
            failed_students.append(student)
        return failed_students

student1 = Student("Giorgi", [75, 85, 92])
student2 = Student("Nina", [60, 70, 80])
student3 = Student("Sali", [45, 55, 65])
student4 = Student("Demna", [90, 80, 88])
student5 = Student("Eva", [30, 40, 35])

student1.add_grade(95)
student2.add_grade(85)
student3.add_grade(50)
student4.add_grade(92)
student5.add_grade(25)

classroom = Classroom()
classroom.add_student(student1)
classroom.add_student(student2)
classroom.add_student(student3)
classroom.add_student(student4)
classroom.add_student(student5)

print("Top Students:")
for student in classroom.get_top_students():
    print(student)

print("\nFailed Students:")
for student in classroom.get_failed_students():
    print(student)
