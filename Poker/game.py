import random
from cards import Card

RANKS = {
    'RoyalFlush': 900,
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

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        #XXX: Limit to 52 cards, and each Card is unique
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(v, s))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class PokerGame:

    def __init__(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = []
        self.player2 = []
        self.deal()
    
    def __call__(self):
        self.showHands()
        print("Community Cards:")
        for card in self.community_cards(3):
            card.show()
        self.player1 += self.community
        self.player2 += self.community
        print("Player 1 has a", self.winningCondition(self.player1))
        print("Player 2 has a", self.winningCondition(self.player2))

    def deal(self):
        for i in range(2):
            self.player1.append(self.deck.drawCard())
            self.player2.append(self.deck.drawCard())
        
    def community_cards(self, num):
        self.community = []
        for i in range(num):
            self.community.append(self.deck.drawCard())
        return self.community
    
    def showHands(self):
        print("Player 1:")
        for card in self.player1:
            card.show()
        print("Player 2:")
        for card in self.player2:
            card.show()

    def winningCondition(self,player):
        #XXX: Check for winning condition
        def is_high():
            for card in player:
                if card.rank == 14 or card.rank == 1:
                    return True
            return False

        def is_onepair():
            for card in player:
                if list(filter(lambda x: x.rank == card.rank, player)).__len__() == 2:
                    return True
            return False
        
        def is_twopair():
            temp_card = None
            pair_counter = 0
            for card in player:
                if card == temp_card:
                    continue
                if list(filter(lambda x: x.rank == card.rank, player)).__len__() == 2:
                    temp_card = card
                    pair_counter += 1
            if pair_counter == 2:
                return True
            return False
        
        def three_of_a_kind():
            for card in player:
                if list(filter(lambda x: x.rank == card.rank, player)).__len__() == 3:
                    return True
            return False
        
        def is_straight():
            straight_counter = 0
            temp_hand = sorted(player, key=lambda card: card.__dir__())
            for card in temp_hand:
                if list(filter(lambda x: x.rank == card.rank + 1, temp_hand)).__len__() == 1:
                    straight_counter += 1
            if straight_counter == 5:
                return True
            return False

        def is_flush():
            for card in player:
                if list(filter(lambda x: x.suit == card.suit, player)).__len__() == 5:
                    return True
            return False

        def is_fullhouse():
            if three_of_a_kind() and is_onepair():
                return True
            return False

        def is_four_of_a_kind():
            for card in player:
                if list(filter(lambda x: x.rank == card.rank, player)).__len__() == 4:
                    return True
            return False

        def is_straightflush():
            if is_straight() and is_flush():
                return True
            return False
        
        def is_royalflush():
            if is_straightflush() and is_high():
                return True
            return False

        is_methodes = {
            is_royalflush: RANKS['RoyalFlush'],
            is_straightflush: RANKS['StraightFlush'],
            is_four_of_a_kind: RANKS['Quads'],
            is_fullhouse: RANKS['FullHouse'],
            is_flush: RANKS['Flush'],
            is_straight: RANKS['Straight'],
            three_of_a_kind: RANKS['Set'],
            is_twopair: RANKS['TwoPairs'],
            is_onepair: RANKS['Pair'],
            is_high: RANKS['High']
        }

        
        for methode in is_methodes.keys():
            if methode():
                return is_methodes[methode]
        return 0
    