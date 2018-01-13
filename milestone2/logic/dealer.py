class Dealer(object):
    hand_total = 0

    def __init__(self, name):
        self.hand = []
        self.name = name
        self.pool = 200
        self.current_bet = 0

    def add_to_hand(self, card):
        self.hand.append(card)
        self.hand_total += card.get_value()

    def get_hand_total(self):
        return self.hand_total

    def has_soft_option(self):
        if any(x.name == 'Ace' for x in self.hand):
            ace = next((card for card in self.hand if card.name == 'Ace' and card.get_value() == 11), None)

            if ace is not None:
                ace.toggle_hardsoft()

    def place_bet(self, bet):
        if bet > self.pool:
            print 'You cant bet more than you have!'
        else:
            self.pool -= bet
            self.current_bet = bet

    def add_to_pool(self, amount):
        self.pool += amount