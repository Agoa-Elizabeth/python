def students_details():
    print("Welcome to the Student Records System!\n")
    
    students_list = []
    num = int(input("Enter number of student entries: "))   
   
    for _ in range(num):
        students = {}
        students["name"] = input("Enter student's name: ")
        students["age"] = int(input("Enter student's age: "))
        students["gender"] = input("Enter student's gender: ")
        students["school"] = input("Enter name of school: ")
        students["program"] = input("Enter your program: ")
        students["yearofstudy"] = int(input("Enter student's year of study: "))
        students["test1"] = int(input("Enter Test 1 marks: "))
        students["test2"] = int(input("Enter Test 2 marks: "))
        students["coursework"] = int(input("Enter coursework marks: "))
        students["exam"] = int(input("Enter exam marks: "))

        students["bestmark"] = bestmark(students["test1"], students["coursework"])
        students["finalmark"] = finalmark(students["bestmark"], students["exam"])

        students_list.append(students)
    
    return students_list

def bestmark(test1, coursework):
    return ((test1 + coursework) / 2) * 0.4

def finalmark(bestmark, exam):
    return bestmark + (exam * 0.6)

# Run the function
students = students_details()

# Print student records
print("\nStudent Records:")
for student in students:
    print(student)
