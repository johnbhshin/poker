# poker file

from card import Card, Deck
from itertools import combinations

scores = {'Royal Straight Flush':100, 'Straight Flush':90, 'Four Card':80, 'Full House':70, 'Flush':60,
          'Straight':50, 'Triple':40, 'Two Pair':30, 'One Pair':20, 'High Card':10}

def review_hand(five_cards):
    rank_bucket = []
    is_flush = True
    is_straight = True
    is_royal_straight_flush = False

    # creat bucket for each rank with sorted cards

    sorted_by_rank = sorted(five_cards, key=lambda x: x.rank_value)

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

    # Royal straight flush
    if (is_straight and is_flush):
        # 10,J,Q,K,A
        if (sorted_by_rank[0].rank_value == 10 and sorted_by_rank[-1].is_ace):
            is_royal_straight_flush = True

    return rank_bucket, is_straight, is_flush, is_royal_straight_flush

def test_cards():
    deck = Deck()
    deck.shuffle()

    cards = []
    for i in range(5):
        card = deck.deal()
        cards.append(card)

    rank_bucket, is_straight, is_flush, is_royal_straight_flush = review_hand(cards)
    print('total # of bucket {}'.format(len(rank_bucket)))
    print('straight is {}, flush is {}'.format(is_straight, is_flush))

    for bucket in rank_bucket:
        for card in bucket:
             print(card)

if __name__ == "__main__":
    test_cards()