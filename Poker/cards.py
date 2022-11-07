cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ss = ["H", "D", "C", "S"]
RANKS = {
    'StraightFlush': 800,
    'Quads': 700,
    'FullHouse': 600,
    'Flush': 500,
    'Straight': 400,
    'Set': 300,
    'TwoPairs': 200,
    'Pair': 100,
    'High': 50
}


class Card:
    def __init__(self, rank: int, suit: str):
        self.rank = rank
        self.suit = suit

    def get_card_by_name(self):
        if self.rank == 1 or self.rank == 14:
            return "Ace"
        elif self.rank == 11:
            return "Jack"
        elif self.rank == 12:
            return "Queen"
        elif self.rank == 13:
            return "King"
        else:
            return str(self.rank)

    def show(self):
        print("{} of {}".format(self.get_card_by_name(), self.suit))
