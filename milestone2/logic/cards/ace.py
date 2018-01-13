from card import Card


class Ace(Card):

    def __init__(self, value, name, suit):
        super(Ace, self).__init__(value, name, suit)
        self.hard_soft_ind = False
        self.value = 1

    def toggle_hardsoft(self):
        self.hard_soft_ind = not self.hard_soft_ind
        if self.hard_soft_ind:
            self.value = 11
        else:
            self.value = 1

    def get_value(self):
        return self.value