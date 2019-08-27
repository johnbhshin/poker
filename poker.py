from card import Card
from score import PokerScore, review_score
from itertools import combinations

class PokerPlayer:

    def __init__(self):
        self.seven_cards = []

    def add_card(self, card):
        self.seven_cards.append(card)
        if (len(self.seven_cards) > 7):
            raise Exception('No more than seven cards')

    def review_all_fiver_hands(self):
        if (len(self.seven_cards) != 7):
            raise Exception('Need seven cards')

        scores = []
        for comb_cards in list(combinations(self.seven_cards, 5)):
            pokerScore = review_score(comb_cards)
            scores.append(pokerScore)

        sorted_poker_scores = sorted(scores, key=lambda x: x.get_total_score(), reverse=True)
        return sorted_poker_scores

