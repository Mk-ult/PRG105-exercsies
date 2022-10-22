# Ask the user how many students are in their class
# Get the student's name and final grade
# Store the answers in a two-dimensional list, display the list, then write the list to the grades.txt file in a comma
# Separated format using quotes around the string values.


total_students = input("How many do you need to enter grades for? ")
student_grades = []
student_name = []
final_list = []
student_file = open("grades.txt", "w")


for i in range(int(total_students)):
    student_grades.append([])
    student_grades[i].append(input("Enter the student's name: "))
    student_grades[i].append(input("Enter the student's grade: "))
    student_file.write(str(student_grades[i]) + " ")

student_file.close()
print(student_grades)
