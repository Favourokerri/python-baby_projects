from class_quiz import Student
from student_details import get_first_name
from student_details import get_last_name
from student_details import get_age
from student_details import get_sex
from student_details import score
from questions import quiz

def get_details():
    first_name = get_first_name()
    last_name = get_last_name()
    age = get_age()
    sex = get_sex()
    student_score = score()
    return Student(first_name, last_name, age, sex, student_score)



def start_quiz():
    print("Are you ready for this quiz?")
    while True:
        try:
            start = input("Enter start [YES/NO]: ").lower()
            if  start == "yes":
                print("starting session")
                quiz()
            elif start == "no":
                print("Alright, come back when you are ready 👍")
                quit()
            if not start or (start != "yes" and "no"):
                raise ValueError
        except ValueError:
            print("....please enter [YES/NO]")
        else:
            break
        
    

