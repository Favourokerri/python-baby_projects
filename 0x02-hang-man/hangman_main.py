from hangman_func import play_game
from about_game import about_game
def main():
    go_back = True
    while go_back == True:
        print("___________WELCOME TO GAME PLAY🙌🐱‍👤🐱_____________", end = "\n")
        print("1)   Play game")
        print("2)   about game")
        print("__________________")
        ans = input("enter [1/2]: ")

        if ans == "1":
            play_game()
        elif ans == "2":
            about_game()
        print("____________________")    
        con = input("Goback [Y/N]: ").lower
    if con == "y":
        go_back = True
    else:
        go_back = False


if __name__ == "__main__":
    main()