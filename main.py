class Board:
    def __init__(self):
        self.winner = None
        self.game_over = None
        self.board = [' '] * 9
        self.counter = 0

    def display_board(self):
        print(" %s | %s | %s" % (self.board[0], self.board[1], self.board[2]))
        print("-------------")
        print(" %s | %s | %s" % (self.board[3], self.board[4], self.board[5]))
        print("-------------")
        print(" %s | %s | %s" % (self.board[6], self.board[7], self.board[8]))

    def update_cell(self, choice, player):
        position = choice - 1
        if self.board[position] == " ":
            self.board[position] = player
            self.counter += 1
            return True
        else:
            return False

    def check_tie(self):
        if self.counter == 9:
            return True

        return False

    def is_winner(self, player):
        combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 4, 8], [0, 4, 8], [2, 4, 6]
        ]

        for combo in combos:
            result = True
            for cell_no in combo:
                if self.board[cell_no] != player:
                    result = False
            if result == True:
                return True

        return False


board = Board()

while True:

    board.display_board()
    x_choice = int(input("\nX) Please choose 1 - 9. > "))
    while board.update_cell(x_choice, "X") == False:
        print(board.update_cell(x_choice, "X"))
        print('This cell is already occupied')
        x_choice = int(input("\nX) Please choose 1 - 9. > "))
    if board.is_winner("X"):
        print("X win")
        break

    if board.check_tie():
        print("Tie game")
        break

    board.display_board()
    o_choice = int(input("\nO) Please choose 1 - 9. > "))

    while board.update_cell(o_choice, "O") == False:
        print('This cell is already occupied')
        o_choice = int(input("\nO) Please choose 1 - 9. > "))
    if board.is_winner("O"):
        print("O win")
        break

    if board.check_tie():
        print("Tie game")
        break
