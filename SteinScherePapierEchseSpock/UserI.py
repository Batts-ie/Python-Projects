import requests

import gamelogic_a
import gamelogic_m
import mysql.connector


def againstAI():
    print("Difficulty of the AI")
    print("e ... Easy AI")  # using Random numbers
    print("m ... Medium AI")  # 20 entries in database
    print("h ... Hard AI")  # database
    print("b ... back to game menu")
    usinput = input("Choose your option: \n")
    usinput = usinput.lower()
    if usinput == "e":
        gamelogic_a.game("e")
    elif usinput == "m":
        gamelogic_a.game("m")
    elif usinput == "h":
        gamelogic_a.game("h")
    elif usinput == "b":
        mainmenu()
    else:
        print("Wrong input please try again")
        againstAI()


def multiplayer():
    print("Multiplayer Mode")
    print("m ... play against a friend [1v1]")
    print("b ... back to game menu")
    usinput = input("Choose your option: \n")
    usinput = usinput.lower()
    if usinput == "m":
        gamelogic_m.game()
    elif usinput == "b":
        gamemenu()
    else:
        print("Wrong input please try again")
        multiplayer()
    pass


def gamemenu():
    print("Choose your playmode")
    print("a ... Against AI")
    print("m ... Against other players on the same PC")
    print("b ... Back to the menu")
    usinput = input("Choose your option: \n")
    usinput = usinput.lower()
    if usinput == "a":
        againstAI()
    elif usinput == "m":
        multiplayer()
    elif usinput == "b":
        mainmenu()
    else:
        print("Wrong input please try again")
        gamemenu()


def stats():
    print("y ... Showing stats")
    print("b ... Back to the menu")
    usinput = input("Choose your option: \n")
    usinput = usinput.lower()
    if usinput == "y":
        conn = mysql.connector.connect(host="localhost", user="swp_rubner", password="swp_rubner202223",
                                       database="swp_rubner_stpes")
        sql = "select player_hand, COUNT(player_hand) AS MOST_TAKEN_HAND FROM GAMES GROUP BY player_hand ORDER BY MOST_TAKEN_HAND DESC LIMIT 1;"
        sql2 = "SELECT sum(has_player_won)/count(has_player_won) from games;"
        con_cursor = conn.cursor()
        con_cursor.execute(sql)
        result_chosen_rate = con_cursor.fetchone()
        con_cursor.execute(sql2)
        print("Here can you see your statistic:")
        print(result_chosen_rate)
        result = con_cursor.fetchone()
        print("The users win rate is: " + str(result[0]) + "%")
        print("The users most chosen hand is " + gamelogic_a.numbertoString(result_chosen_rate[0]) +
              ". It got chosen " + str(result_chosen_rate[1]) + " times")
        print("\nb ... Back to menu")
        print("e ... Exit the game")
        usinput = input("Choose your option: \n")
        usinput = usinput.lower()
        if usinput == "b":
            mainmenu()
        elif usinput == "e":
            print("Goodbye have a nice day")
    elif usinput == "b":
        mainmenu()
    else:
        print("Wrong input please try again")
        stats()


def send_to_flask():
    conn = mysql.connector.connect(host="localhost", user="swp_rubner", password="swp_rubner202223",
                                   database="swp_rubner_stpes")
    conn_cursor = conn.cursor()
    sql = "select player_hand, count(player_hand) from games group by player_hand;"
    conn_cursor.execute(sql)
    result = conn_cursor.fetchone()
    while result is not None:
        print(result)
        response = requests.post(
            "http://127.0.0.1:8888/add",
            json={
                "hand": result[0],
                "count": result[1]
            }
        )
        print(response.text)
        result = conn_cursor.fetchone()


def mainmenu():
    print("Welcome to rock-paper-scissors-lizard-spock")
    print("p ... playing the game")
    print("s ... look at the statistics")
    print("f ... send to flask-api")
    print("e ... exiting the game")
    usinput = input("Choose your option: \n")
    usinput = usinput.lower()
    if usinput == "e":
        print("Goodbye have a nice day")
    elif usinput == "p":
        gamemenu()
    elif usinput == "s":
        stats()
    elif usinput == "f":
        send_to_flask()
        mainmenu()
    else:
        print("Wrong input please try again")
        mainmenu()
