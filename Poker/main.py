from game import PokerGame, Deck

statistics = {
    'RoyalFlush': 0,
    'StraightFlush': 0,
    'Quads': 0,
    'FullHouse': 0,
    'Flush': 0,
    'Straight': 0,
    'Set': 0,
    'TwoPairs': 0,
    'Pair': 0,
    'High': 0
}


def do_statistics(rounds: int = 100000):
    pg = PokerGame()
    for i in range(rounds):
        pg.deck = Deck()
        pg.deck.shuffle()
        pg.player1 = []

        for j in range(5):
            pg.player1.append(pg.deck.drawCard())
        #        pg.showHands()
        result = pg.winningCondition(pg.player1)
        statistics[result] += 1
        pass


def do():
    rounds = int(input("How many rounds do you want to play?: "))
    do_statistics(rounds)
    print(statistics)
    for key in reversed(statistics.keys()):
        print(key + ":" + str(statistics[key] / rounds * 100) + "%")
        # game = PokerGame()
        # game()


if __name__ == "__main__":
    do()
