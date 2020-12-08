import json
import random
import LinkedList
import user


def data_load():
    with open("data.json") as f:
        data = json.load(f)
    return data


def register():
    data = data_load()
    User = input("Enter name for User: ")
    Userpassword = input("Enter password for User: ")
    for i in data["user_base"].keys():
        if User == i:
            print("Already exists")
    else:
        data["user_base"][User] = [Userpassword, 0]
        with open("data.json", 'w') as file:
            file.write(json.dumps(data))

    response = input("Do you want to register anoother user")

    if response == "yes":
        register()


def login():
    data = data_load()
    while True:
        username = input('What is your username? ')
        password = input('What is your password? ')
        for user in data['user_base'].keys():
            if username == user:
                while True:
                    if data['user_base'][username][0] == password:
                        print(f'Welcome, {username} you have successfully logged in.')
                        return username
                    else:
                        print("Incorrect password")
                        password = input('What is your password?')
        else:
            print("Your username is wrong.")


def roll(name):
    points = 0

    Roll1 = random.randint(1, 6)
    print(f'{name}, your first roll is {Roll1}')

    Roll2 = random.randint(1, 6)

    print(f'{name}, your second roll is {Roll2}')

    Rollsum = Roll1 + Roll2

    points = points + Rollsum
    if Rollsum % 2 == 0:
        points = points + 2

    if Roll1 == Roll2:
        print("Since you have equal rolls, you get a chance for an extra roll")
        Roll3 = random.randint(1, 6)
        print(f"Your have {Roll3} added to your points")
        points = points + Roll3
    print(f"{name}, your total points are {points}")
    return (points)


def decisive(pl1roll, pl2roll, player1, player2):
    haxtoxiAnun = ""
    if pl1roll > pl2roll:
        print(f"{player1} has won the game!")
        haxtoxiAnun = player1
    elif pl1roll < pl2roll:
        print(f"{player2} has won the game!")
        haxtoxiAnun = player2

    else:
        print("Your total points are equal, an extra round will show the winner")
        while pl1roll == pl2roll:
            decisive1 = random.randint(1, 6)
            decisive2 = random.randint(1, 6)
            Player1Roll = decisive1
            Player2Roll = decisive2
            if decisive2 < decisive1:
                print(f"{player1} has won the game!")
                haxtoxiAnun = player1
                break
            elif decisive2 > decisive1:
                print(f"{player2} has won the game!")
                haxtoxiAnun = player2
                break
    add(haxtoxiAnun)


def add(haxtoxiAnun):
    data = data_load()
    a = int(data["user_base"][haxtoxiAnun][1]) + 1
    data["user_base"][haxtoxiAnun][1] = a

    with open("data.json", 'w') as file:
        file.update(json.dumps(data))


def printLeaderboard():
    usersdict = {}
    arrayOfScores = []
    data = data_load()
    for i in data["user_base"].keys():  # "babken"
        usersdict[data["user_base"][i][1]] = i  # key:value
        arrayOfScores.append(data["user_base"][i][1])

    for i in range(0, len(arrayOfScores)):
        for y in range(0, len(arrayOfScores) - 1):
            if arrayOfScores[y] > arrayOfScores[y + 1]:
                tmp = arrayOfScores[y]
                arrayOfScores[y] = arrayOfScores[y + 1]
                arrayOfScores[y + 1] = tmp

    for key in arrayOfScores:
        print(f"{usersdict[key]} : {key}")


def printLeaderboardWithLinkedList():
    ourList = LinkedList.LinkedList()
    arrayOfScores = []
    data = data_load()
    for i in data["user_base"].keys(): #babken
        us = user.User(i, data["user_base"][i][0], data["user_base"][i][1]) #name: "babken", pass: "567", score: "3"
        ourList.addNode(us)
        arrayOfScores.append(us.score)

    for i in range(0, len(arrayOfScores)):
        for y in range(0, len(arrayOfScores) - 1):
            if arrayOfScores[y] > arrayOfScores[y + 1]:
                tmp = arrayOfScores[y]
                arrayOfScores[y] = arrayOfScores[y + 1]
                arrayOfScores[y + 1] = tmp

    for key in arrayOfScores:
            print(f"{data['user_base'][key]} : {key}")
