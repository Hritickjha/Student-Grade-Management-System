"""""
Dictionary
collection - key+value = pair = data 1

left-side = key
right-side = value
{key1:value1, key2:value2}

"""
#var = {'key1':100, 'key2':200}
#print(var)

""""
add
update
delete
view
exit
"""
"""""
# create  a dictionary
student = {
    'Raju':100,
    'krishna':200,
}
#Accessing a element
#print(student['krishna'])

#Update
#student['krishna'] = 300
#print(student)

#delete
del student['krishna']
print(student)"""

#Initialising dictionary
student_grades = { }

#Add a new student
def add_student(name, grade):
    student_grades[name] = grade
    #[Hritick] = 100
    print(f"Added {name} with a {grade}")
    #Added Hritick with a 100
    
#Update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        #Hritick = 200
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found!")
#Delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")
        
#view all students
def display_all_student():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}:{grade}")
    else:
        print("No students found/added")
def main():
    while True:
        print('\n Student Grades Management System')
        print("1.Add student")
        print("2.Update student")
        print("3.Delete student")
        print("4.view student")
        print("5.Exit")
        
        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)
        elif choice == 4:
            display_all_student()
        elif choice == 5:
            print("Thank you for using the system")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()