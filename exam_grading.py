'''Python Program which asks the instructor to enter a student's details (namely, Name, Roll
Number), and the score secured by the student in three subjects (namely in Physics, Chemistry and
Maths). The program should then process this data and compute the grade for each subject and also the
overall grade.'''
'''The grade should be computed based on the following criteria:
- Score >= 90: Grade A
- 80 <= Score < 90: Grade B
- 70 <= Score < 80: Grade C
- 60 <= Score < 70: Grade D
- Score < 60: Grade F'''

# Take input for student name , roll number etc..
student_name = str (input("Enter Student Name: "))
roll_num = int (input("Enter Roll No.: "))
marks_maths = int (input("Enter marks in Maths: "))
marks_physics = int (input("Enter marks in Physics: "))
marks_chemistry = int (input("Enter marks in Chemistry: "))
marks_avg = ( marks_maths + marks_physics + marks_chemistry ) / 3

# Create lists for individual marks and mean and also for grades
marks = [marks_maths, marks_physics, marks_chemistry, marks_avg]
grades = [""] * len(marks)


# Convert subject marks to grade and save in an array
for i in range(4):
    if marks[i] >= 90 :
        grades[i] = "A"
    elif 80 <= marks[i] < 90 :
        grades[i] = "B"
    elif 70 <= marks[i] < 80 :
        grades[i] = "C"
    elif 60 <= marks[i] < 70 :
        grades[i] = "D"
    else :
        grades[i] = "F"

# Print grade card for given student
print("Student Name:",student_name)
print("Student Roll:",roll_num)
print("Grade in Maths:",grades[0])
print("Grade in Physics:",grades[1])
print(f"Grade in Chemistry: {grades[2]}")
print(f"Overall Grade: {grades[3]}")