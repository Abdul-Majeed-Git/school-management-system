import os 
school_data: dict ={
                "school_name": "Abdul Majeed Acedamy",
                "location": "Lahore",
                "established": 1998,
                "students": {
                                "S001": {
                                    "name": "Ali Khan",
                                    "age": 15,
                                    "grade": "10th",
                                    "subjects": ["Math", "Physics","English", "Computer"],
                                    "is_active": True
                                },
                                "S002": {
                                    "name": "Sara Ahmed",
                                    "age": 14,
                                    "grade": "9th",
                                    "subjects": ["Biology", "Chemistry","urdu", "English"],
                                    "is_active": True
                                },
                                "S003": {
                                    "name": "Abdul Majeed",
                                    "age": 21,
                                    "grade": "BSCS",
                                    "subjects": ["Computer Architecture", "Data Structures","Algorithms", "Operating Systems"],
                                    "is_active": True
                                },
                                "S004": {
                                    "name": "Affan",
                                    "age": 22,
                                    "grade": "BSCS",
                                    "subjects": ["Software Engineering", "Database Systems","Web Development", "Computer Networks"],
                                    "is_active": True
                                },
                                 "S005": {
                                    "name": "Adil",
                                    "age": 10,
                                    "grade": "BSCS",
                                    "subjects": ["Introduction to Programming", "Basic Electronics","Digital Logic Design", "Discrete Mathematics"],
                                    "is_active": True
                                },
                                "S006":{
                                    "name": "moe",
                                    "age": 80,
                                    "grade": "PHD in rocket science",
                                    "subject": ["rocket Science","computer","rocket engine"],
                                    "is_active": True
                                }
                            },
                "staff_count": 25,
                "facilities": ["Library", "Science Lab", "Sports Ground"]
            }
school_data["facilities"].append("Cafeteria")
#updating fees status
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_fee_status(data):
    for id,info in data["students"].items():
        if info["age"] > 14:
            info["fee_paid"] = True
        else:
            info["fee_paid"] = False
add_fee_status(school_data)
def main_menu():
    print("="*30)
    print("MAJEED ACEDAMY MANAGEMENT SYSTEM".center(30))
    print("="*30)
    while True:
        #all students name and their grades
        def stud_name_grade(data):
            for id,info in data["students"].items():
                print(f"id :{id} | name:{info['name']} | Grades: {info['grade']}")


        #counting students based on subjects
        def count_subjects(data):
            math_count = 0
            bio_count = 0
            for id,info in data["students"].items():
                if "Math" in info["subjects"]:
                    math_count+=1
                if "Biology" in info["subjects"]:
                    bio_count+=1
            print(f"Total Math Studenst:{math_count:>4}")
            print(f"Total Biology Students:{bio_count}")

        #searching grades and name
        def search_students(data):
            student_id = input("Enter student ID to search for grade (e.g., S001):").capitalize()
            if student_id in data["students"]:
                student_name = data["students"][student_id]["name"]
                student_grade = data["students"][student_id]["grade"]
                print(f"Result: {student_name} is in {student_grade} grade.")
            else:
                print("Error: This ID is not available in record.")

        #find students names base on subject
        def subject(data):
            subject = input("Enter subject name to find student:").capitalize()
            found = False
            for id,info in data["students"].items():
                if subject in info["subjects"]:
                    print(f"ID:{id} | {info['name']} studies {subject}")
                    found = True
            if not found:
                print(f"No student studies {subject} subject.")

        #show result card
        def generate_report_card(data):
            search_id = input("Enter student ID(e.g., S001):").upper()
            if search_id in data["students"]:
                info = data["students"][search_id]
                print("\n"+ "="*30)
                print("Student Report Card".center(30))
                print("="*30)
                print(f"Name:{info["name"]}")
                print(f"Grade:{info['grade']}")
                print(f"Age: {info['age']}")
                subject = ",".join(info['subjects'])
                print(f"Subjects: {subject}")

                status = "Paid" if info["fee_paid"] else "Pending"
                print(f"Fees Status: {status}")
                print("="* 30)
            else:
                print("Student ID not found in our records.")
                print("="*30)
        print("="*20)
        print("OPTION".center(20))
        print("="*20)
        print("1. List Student Names and Grades")
        print("2. Search for a Student")
        print("3. Find Students by Subject")
        print("4. Generate Report Card")
        print("5. Exit")
        print("="*30)
        choice = input("Select your option(1-5):")
        if choice == "1":
            clear()
            stud_name_grade(school_data)
            print("\nPress enter to go back to menu...")
        elif choice == "2":
            clear()
            search_students(school_data)
            input("Press enter to go back to menu....")
        elif choice == "3":
            clear()
            subject(school_data)
            input("Press enter to go back to menu....")
        elif choice == "4":
            clear()
            generate_report_card(school_data)
            input("Press enter to go back to menu....")
        elif choice == "5":
            print("Allah Hafiz")
            break
        else:
            print("Wrong choice!!!")
main_menu() 