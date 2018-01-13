class Card(object):

    def __init__(self, value, name, suit):
        self.value = value
        self.name = name
        self.suit = suit

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    def get_suit(self):
        return self.suit

    def __str__(self):
        return "{0} {1}".format(self.name, self.suit)
