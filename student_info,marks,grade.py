print("Written by Aaron 😀")
##Global variables
number_of_students=0
student_info=[]
grade=""

##subprograms
##get number of students
def number_of_students():
    while True:
        try:
            number_of_students = int(input("Enter the number of students: "))
            if int(number_of_students)<6:
                print("Invalid input")
            else:
                return number_of_students
        except ValueError:
            print("Invalid input")

##get name(called in another function)
def get_name():
    while True:
        name = input("Enter name: ")
        if name:
            return name
        else:
            print("Enter something")

##get marks(called in another function)
def get_marks(name):
    while True:
        marks=input("Enter marks: ")
        if int(marks)<0 and int(marks)>100:
            print("Invalid input")
        else:
            return marks

##get grade(called in another function)
def get_grade(marks):
    if int(marks)<=40:
        grade="F"
    elif int(marks)>=41 and int(marks)<=50:
        grade="P"
    elif int(marks) >=51 and int(marks)<=69:
        grade="M"
    else:
        grade="D"
    return grade

##get student info(callback function)
def get_student_info(number_of_students):
    while True:
        while int(number_of_students)>0:
            number_of_students -= 1
            name=get_name()
            marks=get_marks(name)
            grade=get_grade(marks)
            student_info.append((name,marks,grade))
        return student_info


##display results
def display_results(student_info):
    sorted_student_info=sorted(student_info,key=lambda X:X[1], reverse=True)
    for row in sorted_student_info:
        print(row)

##main
number_of_students=number_of_students()
student_info=get_student_info(number_of_students)
display_results(student_info)

                        
                            
