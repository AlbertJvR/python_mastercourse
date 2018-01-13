class GameLogic(object):
    """
    This class contains all the game logic
    """
    def __init__(self):
        self.board = [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
        self.x_max = 2
        self.y_max = 2
        self.player_turn = 0
        self.move_count = 0

        self.player_symbols = ['X', 'O']

    def toggle_turn(self):
        if self.player_turn == 0:
            self.player_turn = 1
        else:
            self.player_turn = 0

    def print_board(self):
        # Print the top line
        x = -1
        y = -1

        while y < 3:
            row = ''
            if x == -1 and y == -1:
                print '   ' + '1'.center(3, ' ') + '2'.center(3, ' ') + '3'.center(3, ' ')
            else:
                row += '{}'.format(y + 1).center(3, ' ')
                while x < 3:
                    row += self.board[x][y].center(3, ' ')
                    x += 1

            print row

            x = 0
            y += 1

    def make_move(self):
        valid_loc = False
        inx = None
        iny = None

        while not valid_loc:
            input = raw_input('Player {} enter location: '.format(self.player_turn + 1)).split(' ')

            inx = int(input[0])
            iny = int(input[1])

            # check if the indicated location is empty
            if self.board[inx - 1][iny - 1] == '~':
                valid_loc = True
            else:
                print 'Location occupado! Try again noob!'

        # Set the indicated location to the current players symbol
        self.board[inx - 1][iny - 1] = self.player_symbols[self.player_turn]

        self.move_count += 1

        # check column
        col_count = 0
        while col_count < 3:
            if self.board[inx - 1][col_count] != self.player_symbols[self.player_turn]:
                break
            if col_count == 2:
                return 1

            col_count = col_count + 1

        # check row
        col_count = 0
        while col_count < 3:
            if self.board[col_count][iny - 1] != self.player_symbols[self.player_turn]:
                break
            if col_count == 2:
                return 1

            col_count = col_count + 1

        # check natural diagonal
        if inx == iny:
            col_count = 0
            while col_count < 3:
                if self.board[col_count][col_count] != self.player_symbols[self.player_turn]:
                    break
                if col_count == 2:
                    return 1

                col_count = col_count + 1

        # check anti diagonal
        if (inx - 1) + (iny - 1) == 2:
            col_count = 0
            while col_count < 3:
                if self.board[col_count][2 - col_count] != self.player_symbols[self.player_turn]:
                    break
                if col_count == 2:
                    return 1

                col_count = col_count + 1

        if self.move_count == 8:
            return 3

        return 2

    def start_game(self):
        """
        This is the main function that launches the game
        :return: void
        """

        terminate = False

        while not terminate:
            result = self.make_move()

            self.print_board()

            if result == 1:
                print 'The winner is {}'.format(self.player_symbols[self.player_turn])
                terminate = True
            elif result == 3:
                print 'This match seems to be a draw'

            self.toggle_turn()



