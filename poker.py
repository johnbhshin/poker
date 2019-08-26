# poker file

from card import Card, Deck
from itertools import combinations

scores = ('Royal Straight Flush', 'Straight Flush', 'Four Card', 'Full House', 'Flush',
          'Straight', 'Triple', 'Two Pair', 'One Pair', 'High Card')
score_values = {'Royal Straight Flush':1000, 'Straight Flush':900, 'Four Card':800, 'Full House':700, 'Flush':600,
          'Straight':500, 'Triple':400, 'Two Pair':300, 'One Pair':200, 'High Card':100}

class PokerScore:
    def __init__(self, score = 'High Card'):
        if (scores.count(score) == 0):
            raise Exception('Undefined Score')
        self.score = score
        self.cards = []

    def __str__(self):
        print('Score is {}({})'.format(self.score, score_values[self.score]))
        for card in cards:
            print(card)

    def set_score(self, score):
        if (scores.count(score) == 0):
            raise Exception('Undefined Score')
        self.score = score

    def set_score_cards(self, cards):
        self.cards = cards

    def add_score_cards(self, cards):
        self.cards.extend(cards)

def review_hand(five_cards):
    rank_bucket = []
    is_flush = True
    is_straight = True

    # creat bucket for each rank with sorted cards

    sorted_by_rank = sorted(five_cards, key=lambda x: x.rank_value)

    pokerScore = PokerScore('High Card')

    first_card = sorted_by_rank[0]
    first_suit = first_card.suit
    last_rank = first_card.rank_value

    rank_bucket.append([first_card])

    for card in sorted_by_rank[1:]:
        current_rank = card.rank_value

        if (card.suit != first_suit):
            is_flush = False

        if (current_rank != last_rank + 1):
            is_straight = False

        if (current_rank != last_rank):
            rank_bucket.append([card])
            last_rank = current_rank
        else:
            rank_bucket[-1].append(card)

    # Ace handling
    if (len(rank_bucket) == 5):
        if (sorted_by_rank[-1].is_ace and
            sorted_by_rank[-2].rank_value == 5 and
            sorted_by_rank[0].rank_value == 2):
            is_straight = True

    # straight or flush (no pair)
    if (is_straight or is_flush):
        if (is_straight and is_flush):
            # Royal straight flush
            # 10,J,Q,K,A
            if (sorted_by_rank[0].rank_value == 10 and sorted_by_rank[-1].is_ace):
                pokerScore.set_score('Royal Straight Flush')
                pokerScore.set_score_cards(sorted_by_rank)
            else:
                pokerScore.set_score('Straight Flush')
                pokerScore.set_score_cards(sorted_by_rank)

        if (is_flush):
            pokerScore.set_score('Flush')
            pokerScore.set_score_cards(sorted_by_rank)
        elif (is_straight):
            pokerScore.set_score('Straight')
            pokerScore.set_score_cards(sorted_by_rank)

        return pokerScore
    else:
        pokerScore.set_score_cards(sorted_by_rank)
        return pokerScore

def test_cards():
    deck = Deck()
    deck.shuffle()

    cards = []
    for i in range(5):
        card = deck.deal()
        cards.append(card)

    pokerScore = review_hand(cards)
    print('Poker Score is {}'.format(pokerScore.score))
# poker file

from card import Card, Deck
from itertools import combinations

scores = ('Royal Straight Flush', 'Straight Flush', 'Four Card', 'Full House', 'Flush',
          'Straight', 'Triple', 'Two Pair', 'One Pair', 'High Card')
score_values = {'Royal Straight Flush':1000, 'Straight Flush':900, 'Four Card':800, 'Full House':700, 'Flush':600,
          'Straight':500, 'Triple':400, 'Two Pair':300, 'One Pair':200, 'High Card':100}

class PokerScore:
    def __init__(self, score = 'High Card'):
        if (scores.count(score) == 0):
            raise Exception('Undefined Score')
        self.score = score
        self.cards = []

    def __str__(self):
        returnStr = 'Score is ' + self.score + ' ' + str(score_values[self.score])
        for card in self.cards:
            returnStr += '\n' + card.rank + '(' + str(card.rank_value) + ') of ' + card.suit
        return returnStr

    def set_score(self, score):
        if (scores.count(score) == 0):
            raise Exception('Undefined Score')
        self.score = score

    def set_score_cards(self, cards):
        self.cards = cards

    def add_score_cards(self, cards):
        self.cards.extend(cards)

def review_hand(five_cards):
    rank_bucket = []
    is_flush = True
    is_straight = True

    # creat bucket for each rank with sorted cards

    sorted_by_rank = sorted(five_cards, key=lambda x: x.rank_value)

    pokerScore = PokerScore('High Card')

    first_card = sorted_by_rank[0]
    first_suit = first_card.suit
    last_rank = first_card.rank_value

    rank_bucket.append([first_card])

    for card in sorted_by_rank[1:]:
        current_rank = card.rank_value

        if (card.suit != first_suit):
            is_flush = False

        if (current_rank != last_rank + 1):
            is_straight = False

        if (current_rank != last_rank):
            rank_bucket.append([card])
            last_rank = current_rank
        else:
            rank_bucket[-1].append(card)

    # Ace handling
    if (len(rank_bucket) == 5):
        if (sorted_by_rank[-1].is_ace and
            sorted_by_rank[-2].rank_value == 5 and
            sorted_by_rank[0].rank_value == 2):
            is_straight = True

    # straight or flush (no pair)
    if (is_straight or is_flush):
        if (is_straight and is_flush):
            # Royal straight flush
            # 10,J,Q,K,A
            if (sorted_by_rank[0].rank_value == 10 and sorted_by_rank[-1].is_ace):
                pokerScore.set_score('Royal Straight Flush')
                pokerScore.set_score_cards(sorted_by_rank)
            else:
                pokerScore.set_score('Straight Flush')
                pokerScore.set_score_cards(sorted_by_rank)
        else:
            if (is_flush):
                pokerScore.set_score('Flush')
                pokerScore.set_score_cards(sorted_by_rank)
            elif (is_straight):
                pokerScore.set_score('Straight')
                pokerScore.set_score_cards(sorted_by_rank)

        return pokerScore
    else:
        sorted_rank_bucket = sorted(rank_bucket, key=lambda x: len(x), reverse=True)
        types_of_rank = len(sorted_rank_bucket)
        top_num = len(sorted_rank_bucket[0])

        if (types_of_rank == 4):
            if (top_num == 2):
                pokerScore.set_score('One Pair')
                pokerScore.set_score_cards(sorted_rank_bucket[0])
        elif (types_of_rank == 3):
            if (top_num == 3):
                pokerScore.set_score('Triple')
                pokerScore.set_score_cards(sorted_rank_bucket[0])
            else:
                pokerScore.set_score('Two Pair')
                pokerScore.set_score_cards(sorted_rank_bucket[0])
                pokerScore.add_score_cards(sorted_rank_bucket[1])
        elif (types_of_rank == 2):
            if (top_num == 4):
                pokerScore.set_score('Four Card')
                pokerScore.set_score_cards(sorted_rank_bucket[0])
            else:
                pokerScore.set_score('Full House')
                pokerScore.set_score_cards(sorted_rank_bucket[0])
                pokerScore.add_score_cards(sorted_rank_bucket[1])
        else:
            # High Card, Top card sorted by rank
            pokerScore.set_score('High Card')
            pokerScore.set_score_cards([sorted_by_rank[-1]])

        return pokerScore

def test_cards():
    deck = Deck()
    deck.shuffle()

    cards = []
    for i in range(5):
        card = deck.deal()
        cards.append(card)

    pokerScore = review_hand(cards)
    print(pokerScore)

if __name__ == "__main__":
    test_cards()
