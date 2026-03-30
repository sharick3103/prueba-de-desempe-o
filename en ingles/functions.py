students = []

# we define the function that registers the students
def register_student():
    id_val = int(input(" Enter student identification: "))
    name = input(" Enter student name: ")
    age = int(input(" Enter student age: "))
    course = input(" Enter student course: ")
    status = input(" Enter if the student is active or inactive: ")
    
    # we create a dictionary where each data is shown
    information = { "name" : name, "id" : id_val, "age" : age, "course" : course, "status" : status }
    students.append(information) # we add each data to the end of the students list
    
    # print data
    print("=" * 40)
    print(f" student : {name} ")
    print(f" ID : {id_val} ")
    print(f" age : {age} ")
    print(f" course : {course} ")
    print(f" status : {status} ")
    print("=" * 40)

# we define a function again but this time to consult
def consult_student():
    # if there are no students, it shows that there are no registered students
    if not students:
        print(" There are no registered students ")
    else:
        # if there are, it shows the data saved in the student list
        for i in students:
            print("=" * 60)
            print(f" Student: {i['name']} | id: {i['id']} | age: {i['age']} | course: {i['course']} | status: {i['status']} " )
            print("=" * 60)
# function to update
def update_student():
    try:
        # enter the identification of the student you want to search for
        searched = int(input(" Enter student identification: "))
        # if you put name or letters, an error will occur
    except ValueError:
        print(" You must enter a number ")
        return

    # we go through the list to look for the student
    for student in students:
        # data is updated
        if student["id"] == searched:
            student["name"] = input(" New name: ")
            student["course"] = input(" New course: ")
            student['status'] = input("New status:")
            print(" Data updated ")
            return
    print(" This student has not been found. ")

# we define another function to delete
def delete_student():
    try:
        searched = float(input(" Enter the identification to delete: "))
    except ValueError:
        print(" Error: Enter a valid number. ")
        return
        
    for student in students:
        if student["id"] == searched:
            students.remove(student) # we delete a specific value
            print(f" Student {student['name']} deleted. ")
            return
    print(" This student has not been found. ")