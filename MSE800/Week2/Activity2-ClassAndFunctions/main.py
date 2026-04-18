##Develop a project using one class and a minimum of two functions that can collect the name, age, and student ID for at least three students.
##After collecting the data, print out a list of student names and ages in order.

#Global variable
students = []

 #student class
class Student: 
    def set_data(self, name, age, studentId):
        self.name = name
        self.age = age
        self.studentId = studentId


#Collect Student Data
def student_collection():

    #collect atleast 3 students data
    for i in range(3):
        print(f"Enter Student {i+1} Details ")
        #local variables
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        studentId = input("Enter Student ID: ")

        student = Student()
        student.set_data(name, age, studentId)
        students.append(student)

        print()

#display students sorted by age
def display_sorted_students():
    print("Students List (Name and Age) \n")
    sorted_student_list = sorted(students, key=lambda s: s.age)
    for student in sorted_student_list:
        print(f"{student.name} - {student.age}")

if __name__ == "__main__":
    student_collection()
    display_sorted_students()




    