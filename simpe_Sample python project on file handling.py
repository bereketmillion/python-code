#Information Technology
def add_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    with open("students.txt", "a") as file:
        file.write(f"{student_id},{name},{age}\n")
    print("Student information added successfully.")
def search_student_by_id(student_id):
    with open("students.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if info[0] == student_id:
                return info
    return None
def retrieve_all_students():
    with open("students.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            print(f"Student ID: {info[0]}, Name: {info[1]}, Age: {info[2]}")
def update_student_info(student_id, new_name, new_age):
    updated_info = []
    with open("students.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if info[0] == student_id:
                info[1] = new_name
                info[2] = new_age
            updated_info.append(",".join(info))
    with open("students.txt", "w") as file:
        for updated in updated_info:
            file.write(f"{updated}\n")
    print("Student information updated successfully.")
def delete_student_info(student_id):
    filtered_info = []
    with open("students.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if info[0] != student_id:
                filtered_info.append(",".join(info))
    with open("students.txt", "w") as file:
        for filtered in filtered_info:
            file.write(f"{filtered}\n")
    print("Student information deleted successfully.")
while True:
    print("\n1. Add Student\n2. Search Student\n3. Retrieve All Students\n4. Update Student\n5. Delete Student\n6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student_info()
    elif choice == "2":
        student_id = input("Enter student ID to search: ")
        student_info = search_student_by_id(student_id)
        if student_info:
            print(f"Student found - ID: {student_info[0]}, Name: {student_info[1]}, Age: {student_info[2]}")
        else:
            print("Student not found.")
    elif choice == "3":
        retrieve_all_students()
    elif choice == "4":
        student_id = input("Enter student ID to update: ")
        new_name = input("Enter new name: ")
        new_age = input("Enter new age: ")
        update_student_info(student_id, new_name, new_age)
    elif choice == "5":
        student_id = input("Enter student ID to delete: ")
        delete_student_info(student_id)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")