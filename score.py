from card import Card, Deck

scores = ('Royal Straight Flush', 'Straight Flush', 'Four Card', 'Full House', 'Flush',
          'Straight', 'Triple', 'Two Pair', 'One Pair', 'High Card')
score_values = {'Royal Straight Flush':100, 'Straight Flush':90, 'Four Card':80, 'Full House':70, 'Flush':60,
          'Straight':50, 'Triple':40, 'Two Pair':30, 'One Pair':20, 'High Card':10}

class PokerScore:
    def __init__(self, score = 'High Card'):
        if (scores.count(score) == 0):
            raise Exception('Undefined Score')
        self.score = score
        self.cards = []

    def __str__(self):
        returnStr = 'Score is ' + self.score + ' ' + str(self.get_total_score())
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

    def get_top_card(self):
        return self.cards[-1]

    def get_total_score(self):
        return score_values[self.score]*10 + self.get_top_card().rank_value

def review_score(five_cards):
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
            # Ace is low
            sorted_by_rank[-1].rank_value = 1
            sorted_by_rank.insert(0, sorted_by_rank.pop())

    # straight or flush (no pair)
    if (is_straight or is_flush):
        if (is_straight and is_flush):
            # Royal Straight Flush (10,J,Q,K,A)
            if (sorted_by_rank[0].rank_value == 10 and sorted_by_rank[-1].is_ace):
                pokerScore.set_score('Royal Straight Flush')
                pokerScore.set_score_cards(sorted_by_rank)
            # Straight Flush (not Royal)
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
    # no straight, no flush -> check out pairs
    else:
        ranks_count = len(rank_bucket)
        # No pair -> High Card
        if (ranks_count == 5):
            pokerScore.set_score('High Card')
            pokerScore.set_score_cards([sorted_by_rank[-1]])
            return pokerScore

        # if any pair exist
        sorted_rank_bucket = sorted(rank_bucket, key=lambda x: len(x), reverse=True)
        top_rank_count = len(sorted_rank_bucket[0])

        # 2, 1, 1, 1
        if (ranks_count == 4):
            if (top_rank_count == 2):
                pokerScore.set_score('One Pair')
                pokerScore.set_score_cards(sorted_rank_bucket[0])
        # 3, 1, 1 or 2, 2, 1
        elif (ranks_count == 3):
            if (top_rank_count == 3):
                pokerScore.set_score('Triple')
                pokerScore.set_score_cards(sorted_rank_bucket[0])
            else:
                pokerScore.set_score('Two Pair')
                pokerScore.set_score_cards(sorted_rank_bucket[0])
                pokerScore.add_score_cards(sorted_rank_bucket[1])
        # 4, 1 or 3, 2
        elif (ranks_count == 2):
            if (top_rank_count == 4):
                pokerScore.set_score('Four Card')
                pokerScore.set_score_cards(sorted_rank_bucket[0])
            else:
                pokerScore.set_score('Full House')
                pokerScore.set_score_cards(sorted_rank_bucket[1])
                pokerScore.add_score_cards(sorted_rank_bucket[0])

        return pokerScore
