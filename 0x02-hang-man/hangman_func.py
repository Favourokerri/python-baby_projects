from play_game_func import who_To_play

def play_game():
    while True:
        try:
            play = input("are you ready to play?[Y/N]: ").lower()

            if play == "y":
                print("________STARTING GAME_________", end = "\n")
                who_To_play()
                               
            elif play == "n":
                print("alright come back when you are ready")
                quit()
            if not play or (play != "y" and play != "n"):
                raise ValueError
        except ValueError:
            print("________please enter [Y/N]__________")
        else:
            break
