import unittest
from poker import review_hand
from card import Card

class PokerRuleTestCase(unittest.TestCase):

    def test_ace_straight_true(self):
        cards = []
        cards.append(Card('Hearts', 'Ace'))
        cards.append(Card('Spades', 'Two'))
        cards.append(Card('Hearts', 'Three'))
        cards.append(Card('Hearts', 'Four'))
        cards.append(Card('Clubs', 'Five'))

        rank_bucket, is_straight, is_flush, is_royal_straight_flush = review_hand(cards)

        self.assertEqual(is_straight, True)

    def test_ace_straight_false(self):
        cards = []
        cards.append(Card('Hearts', 'Ace'))
        cards.append(Card('Spades', 'Two'))
        cards.append(Card('Hearts', 'Two'))
        cards.append(Card('Hearts', 'Four'))
        cards.append(Card('Clubs', 'Five'))

        rank_bucket, is_straight, is_flush, is_royal_straight_flush = review_hand(cards)

        self.assertEqual(is_straight, False)

    def test_royal_straight_flush_true(self):
        cards = []
        cards.append(Card('Spades', 'Ten'))
        cards.append(Card('Spades', 'Jack'))
        cards.append(Card('Spades', 'Queen'))
        cards.append(Card('Spades', 'King'))
        cards.append(Card('Spades', 'Ace'))

        rank_bucket, is_straight, is_flush, is_royal_straight_flush = review_hand(cards)

        self.assertEqual(is_royal_straight_flush, True)

    def test_royal_straight_flush_false(self):
        cards = []
        cards.append(Card('Spades', 'Ten'))
        cards.append(Card('Hearts', 'Jack'))
        cards.append(Card('Spades', 'Queen'))
        cards.append(Card('Spades', 'King'))
        cards.append(Card('Spades', 'Ace'))

        rank_bucket, is_straight, is_flush, is_royal_straight_flush = review_hand(cards)

        self.assertEqual(is_straight, True)
        self.assertEqual(is_royal_straight_flush, False)

if __name__ == '__main__':
    unittest.main()
