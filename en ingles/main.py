from functions import ( register_student, consult_student, update_student, delete_student )

print("=" * 40)
print(" STUDENT MANAGEMENT ")
print("=" * 40)

# assigned a true variable to control the while
option = True

# show the options that can be performed
while option:
    print(" What Management do you want to perform on the student? ")
    print(" 1. Register a new student. ")
    print(" 2. Consult student list. ")
    print(" 3. Update a student's information. ")
    print(" 4. Delete students. ")
    print(" 5. Exit. ")
    
    management_to_perform = input(" Enter the management you want to perform: ")
    
    if management_to_perform == "1":
        register_student()
    elif management_to_perform == "2":
        consult_student()
    elif management_to_perform == "3":
        update_student()
    elif management_to_perform == "4":
        delete_student()
    elif management_to_perform == "5":
        print("leaving...")
        option = False
    else:
        print(" Invalid option, please enter a number from 1 to 5 ")