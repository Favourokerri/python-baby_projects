def get_int():
    while True:
        try:
            ans = int(input("please enter your choice[1/2]: "))
            if not ans or (ans != 1 and ans != 2):
                raise ValueError 
            return (ans)
        except ValueError:
            print("_____please enter[1/2]_____")
        else:
            break