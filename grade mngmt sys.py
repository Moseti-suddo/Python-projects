import os

print("----Student Grade Management System For Students in Year 2----")
print()


def records_input(): 
    name = input("Enter the name of the student: ")
    student_id = int(input("Enter the student's id: "))
    math = int(input("Enter Maths marks: "))
    english = int(input("Enter English marks: "))
    art = int(input("Enter Art marks: "))
    science = int(input("Enter Science marks: "))
    average = (math + english + art + science) / 4


    if average >= 70 and average <= 100:
        grade = "A"
    elif average >= 60 :
        grade = "B"
    elif average >= 50 :
        grade = "C"
    elif average >= 40 : 
        grade = "D"
    else:
        grade = "F"


    print()    
    student = {
    "Full_name" : f"{name}",
    "Student ID" : f"{student_id}",
    "Marks" : [f"Math = {math}", f"English = {english}", f"Art = {art}", f"Science = {science}"],
    "Average" : f"{average:.2f}",
    "Grade" : f"{grade}"
    }




    file_path = "PYTHON projects/records.txt"
    write_header = not os.path.exists(file_path) or os.path.getsize(file_path) == 0 #Youll write the header only if the file does not exist or the file exists but is empty


    #writing to file
    with open(file_path, "a") as f:
        if write_header:
            f.write(f"{"Full_Name":<30} {"Student ID":<18} {"Math":<15} {"English":<15} {"Art":<15} {"Science":<15} {"Average":<18} {"Grade":<15}")
            f.write("\n" + "-"*139 + "\n")
        f.write(f"{name:<30} {student_id:<18} {math:<15} {english:<15} {art:<15} {science:<15} {average:<18} {grade:<15}")
        f.write("\n" + "-"*139 + "\n")

    #Printing to terminal
    for key , value in student.items():
        print(f"{key} : {value}")

    # with open("PYTHON practice/practice/records.txt", "a") as f:
    #     for key , value in student.items():
    #         f.write(f"{key:<20}: {value}  " )
    #     f.write("\n" + "-"*200 + "\n")



records_input()

