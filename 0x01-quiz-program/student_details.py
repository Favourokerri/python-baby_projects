def get_first_name():
    while True:
        try:
            first_name = input("enter first name: ")
            if not first_name:
                raise ValueError
            return (first_name)
        except ValueError:
            print(".....please fill in this field.....")
        else:
            break

def get_last_name():
    while True:
        try:
            last_name = input("enter last name: ")
            if not last_name:
                raise ValueError
            return (last_name)
        except ValueError:
            print(".....please fill in this field.....")
        else:
            break

def get_age():
    while True:
        try:
            age = int(input("please enter your age: "))
            return (age)
        except ValueError:
            print("......please age must be an integer: ")
        else:
            break

def get_sex():
    while True:
        try:
            sex = input("Enter sex name [M/F]: ").upper()
            if not sex or (sex != "M" and sex != "F"):
                raise ValueError
            return sex
        except ValueError:
            print("Please enter either 'M' or 'F'.")

def score():
    score = 0
    print("your initial score is {:d}".format(score))
    return score