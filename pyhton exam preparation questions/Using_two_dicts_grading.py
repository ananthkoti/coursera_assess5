def getGrade(mark):
    #If marks between 90 to 100:grade'O'
    if mark>=90 and mark<=100:
        return "O"
    #marks between 80 to 90:grade'A+'
    if mark>=80 and mark<90:
        return "A+"
    #marks between 70 to 80:grade'A'
    if mark>=70 and mark<80:
        return "A"
    #marks between 60 to 70:grade'B+'
    if mark>=60 and mark<70:
        return "B+"
    #marks between 50 to 60:grade'B'
    return "B"
# cosidering the two dicts one for storing names and another for marks
studentNames={}
studentMarks={}

# to take details of n number of students
N = int(input("Enter number of students: "))

# for loop to enter the student details one by one
for i in range(N):
    # serial number
    print("Enter Details of student No.", i+1)
    # to take registration number of the student
    registrationNumber = int(input("Enter the registration number of the student: "))
    #  to take name of the student from user
    name = input("Enter the name of the student: ")
    #  to take marks from user
    mark = int(input("Enter the mark of the student: "))
    # to store name for paticular regd number
    studentNames[registrationNumber] = name
    # to check the grade
    grade=getGrade(mark)
    studentMarks[registrationNumber] = [mark,grade]


print(studentNames)
print(studentMarks)
