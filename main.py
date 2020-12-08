import random
import functions


def main():
    while True:

        choice = input("Do you want to register, login or see leaderboard?")
        if choice == "register":
            functions.register()
        elif choice == 'login':
            print("Player 1 please login")
            player1 = functions.login()
            choice1 = input("Do you want to register another player(You will need to login once again)")
            if choice1 == "yes":
                functions.register()
            elif choice1== "no" :
                    print("Player 2 please login")
                    player2 = functions.login()

                    Player1Roll = functions.roll(player1)
                    Player2Roll = functions.roll(player2)

                    functions.decisive(Player1Roll, Player2Roll, player1, player2)
            elif choice == "see leaderboard":
                    functions.printLeaderboard()
            else:
                print('Wrong keyword, please try again.')


main()
