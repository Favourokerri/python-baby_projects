import random
from hangman_stages import stages

def who_To_play():
    while True:
        try:
            play = input("do you want to play with computer [Y/N]: ").lower()
            print("")
            if  play == "y":
                print("___________STARTING SESSION WITH COMPUTER_______________")
                play_computer()
            elif play == "n":
                print("____________STARTING SESSION WITH PEER___________")
            if not play or (play != "y" and play != "n"):
                raise ValueError
        except ValueError:
            print("____________please enter [Y/N]______________")
        else:
            break


def play_computer():
    print("this is going to be a guessing game about friuts") 
    fruits = ['apple', 'orange', 'pineapple', 'pear', 'pawpaw', 'banana'] #list of avaliable friuts
    chosen_word = random.choice(fruits) #the friut randomly chosen
    display = []
    for i in range(len(chosen_word)):
        display += '_'
        i += 1
    
    game_over = False
    play_again = True
    lives = 7
    print(display)
    while play_again:
        while not game_over:
            guess_letter = input("guess friut word for word: ")
            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess_letter:
                    display[position] = letter
            print(display)
            if guess_letter not in chosen_word:
                lives -= 1
                print("_______oops you gussed wrong you have {:d} lives left________".format(lives), end = "\n")
                print(stages[lives])

            if '_' not in display:
                print("____________you win______________")
                play = input("do you want to try agin?[Y?N]: ").lower()
                if play == "y":
                    play_again = True
                else:
                    play_again = False
                    game_over = True

            elif lives == 0:
                print("_____________oops you lose__________ ")

                play = input("do you want to try agin?[Y?N]: ").lower()
                if play == "y":
                    play_again = True
                elif play == "n":
                    play_again = False