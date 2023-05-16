from student_details import get_first_name
from student_details import get_last_name
from student_details import get_age
from student_details import get_sex
from student_details import score

def get_details():
    get_first_name()
    get_last_name()
    get_age()
    get_sex()
    score()



def start_quiz():
    print("Are you ready for this quiz?")
    start = input("Enter start [start]: ").lower()
    if  start == "start":
        print("starting session")
    

