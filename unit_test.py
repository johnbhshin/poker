import unittest
from card import Card
from score import PokerScore, review_score

class PokerScoreTestCase(unittest.TestCase):

    def test_ace_straight_true(self):
        cards = []
        cards.append(Card('Hearts', 'Ace'))
        cards.append(Card('Spades', 'Two'))
        cards.append(Card('Hearts', 'Three'))
        cards.append(Card('Hearts', 'Four'))
        cards.append(Card('Clubs', 'Five'))

        pokerScore = review_score(cards)

        self.assertEqual(pokerScore.score == 'Straight', True)

    def test_ace_straight_false(self):
        cards = []
        cards.append(Card('Hearts', 'Ace'))
        cards.append(Card('Spades', 'Two'))
        cards.append(Card('Hearts', 'Two'))
        cards.append(Card('Hearts', 'Four'))
        cards.append(Card('Clubs', 'Five'))

        pokerScore = review_score(cards)

        self.assertEqual(pokerScore.score == 'Straight', False)

    def test_royal_straight_flush_true(self):
        cards = []
        cards.append(Card('Spades', 'Ten'))
        cards.append(Card('Spades', 'Jack'))
        cards.append(Card('Spades', 'Queen'))
        cards.append(Card('Spades', 'King'))
        cards.append(Card('Spades', 'Ace'))

        pokerScore = review_score(cards)

        self.assertEqual(pokerScore.score == 'Royal Straight Flush', True)

    def test_royal_straight_flush_false(self):
        cards = []
        cards.append(Card('Spades', 'Ten'))
        cards.append(Card('Hearts', 'Jack'))
        cards.append(Card('Spades', 'Queen'))
        cards.append(Card('Spades', 'King'))
        cards.append(Card('Spades', 'Ace'))

        pokerScore = review_score(cards)

        self.assertEqual(pokerScore.score == 'Straight', True)

if __name__ == '__main__':
    unittest.main()
