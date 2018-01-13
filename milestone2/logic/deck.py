from logic.cards.number import NumberCard
from logic.cards.face import FaceCard
from logic.cards.ace import Ace
import random


class Deck(object):
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    faces = ('King', 'Queen', 'Jack')
    numbers = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten')

    def __init__(self, num_decks):
        self.deck_list = []
        self.num_decks = num_decks
        self.draw_count = 0

        for z in range(num_decks):
            for i in range(2, 11):
                for k in range(len(self.suits)):
                    self.deck_list.append(NumberCard(i, self.numbers[i - 2], self.suits[k]))

            for i in range(0, 3):
                for k in range(len(self.suits)):
                    self.deck_list.append(FaceCard(10, self.faces[i], self.suits[k]))

            for i in range(len(self.suits)):
                self.deck_list.append(Ace(11, 'Ace', self.suits[i]))

    def shuffle_deck(self):
        random.shuffle(self.deck_list)

    def draw_card(self):
        card = self.deck_list.pop()
        self.deck_list.insert(0, card)
        self.draw_count += 1

        if self.draw_count == len(self.deck_list):
            random.shuffle(self.deck_list)
            self.draw_count = 0

        return card

    def print_deck(self):
        for card in self.deck_list:
            print card
