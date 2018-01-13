from player import Player
from deck import Deck


class GameLogic(object):
    dealer = Player('Vlad')

    def __init__(self, num_of_players):
        self.players = [Player('Player {}'.format(x)) for x in range(0, num_of_players)]
        self.deck = Deck(1)
        print self.players

    def start_game(self):
        print 'Welcome to the Blackjack table noobs!\n'
        print 'Your dealer will be {}'.format(self.dealer.name)

        print 'Lets quickly shuffle the deck, not that it\'s gonna save you losers, lol.'
        self.deck.shuffle_deck()

        print 'The deck is shuffled, let\'s do this!'

        while True:
            print 'Dealing to all players 2 cards...'
            for player in self.players:
                print '{0} \'s current pool is: {1}'.format(player.name, player.pool)
                player_bet = raw_input('Place your bet {} sama:'.format(player.name))

                if int(player_bet) > player.get_pool() > 0:
                    choice = raw_input('You only have {},\n(1)Bet it all, or, (2)Quit like a bitch\nYour choice:')

                    if choice == '1':
                        player.place_bet(int(player_bet))
                    else:
                        self.players.remove(player)
                        continue

                player.add_to_hand(self.deck.draw_card())
                player.add_to_hand(self.deck.draw_card())

                while player.get_hand_total() <= 21:
                    hit_stay = raw_input('Your total {}:\n (1) Hit, (2) Stay : '.format(player.hand_total))
                    if hit_stay == '2':
                        break
                    else:
                        player.add_to_hand(self.deck.draw_card())
                        if player.hand_total > 21:
                            print 'You busted homie! Hand total {}'.format(player.hand_total)
                            break
                else:
                    print 'You busted homie! Hand total {}'.format(player.hand_total)

            print 'Now the dealer gets 2 cards...'
            self.dealer.add_to_hand(self.deck.draw_card())
            self.dealer.add_to_hand(self.deck.draw_card())

            while self.dealer.hand_total < 17:
                self.dealer.add_to_hand(self.deck.draw_card())

            if self.dealer.hand_total > 21:
                print 'dealer loses'
                for player in self.players:
                    player.add_to_pool(player.current_bet * 2)
                    player.empty_hand()
            else:
                for player in self.players:
                    if player.hand_total == self.dealer.hand_total:
                        print '{0} and the dealer are tied on {1}'.format(player.name, player.hand_total)
                        player.add_to_pool(player.current_bet)
                    elif player.hand_total > self.dealer.hand_total:
                        print '{0} has defeated the dodgey dealer'.format(player.name)
                        player.add_to_pool(player.current_bet * 2)

                    player.empty_hand()
