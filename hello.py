students = []
add_confirm = "y"
user_input = ""

while add_confirm == "y":
    add_confirm = input("Do you want to add a student? Enter y/n ")
    if add_confirm == "n":
        continue #If condition is true, it takes flow back to the beginning of iteration.
        print("add process completed")
    
    user_input = input("enter student name: ")

    for s in students:
        if s == user_input:
            print(user_input, "is already a student")
            break
        
    else:
        students.append(user_input)
        print(user_input, "is now added")
        print(students)
