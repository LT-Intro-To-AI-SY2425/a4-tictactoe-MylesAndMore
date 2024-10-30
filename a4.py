# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    def __init__(self):
        self.clear()

    def __str__(self):
        return "\n".join([
            f"{self.board[0]} | {self.board[1]} | {self.board[2]}",
            "--+---+--",
            f"{self.board[3]} | {self.board[4]} | {self.board[5]}",
            "--+---+--",
            f"{self.board[6]} | {self.board[7]} | {self.board[8]}"
        ])

    def make_move(self, player: str, position: int) -> bool:
        """Make a move on the board.
        :param player: the player to make the move, either 'X' or 'O'
        :param position: the position to make the move, an integer between 0 and 8 inclusive\
        :return: True if the move was successful
        """
        if self.board[position] == "*":
            self.board[position] = player
            return True
        return False

    def has_won(self, player: str) -> bool:
        """Check if a player has won.
        :param player: the player to check, either 'X' or 'O'
        :return: True if the given player has won
        """
        winning_combos = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        for combo in winning_combos:
            if all([self.board[i] == player for i in combo]):
                return True
        return False

    def game_over(self) -> bool:
        """
        :return: True if the game is over
        """
        return self.has_won("X") or self.has_won("O") or "*" not in self.board

    def clear(self):
        """Clears the board"""
        self.board = ["*"] * 9


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    brd.clear()

    # Horizontal win
    brd.make_move("X", 0)
    brd.make_move("X", 1)
    brd.make_move("X", 2)
    assert brd.has_won("X") == True
    assert brd.game_over() == True

    brd.clear()

    # Vertical win
    brd.make_move("O", 0)
    brd.make_move("O", 3)
    brd.make_move("O", 6)
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    brd.clear()

    # Diagonal win
    brd.make_move("X", 0)
    brd.make_move("X", 4)
    brd.make_move("X", 8)
    assert brd.has_won("X") == True
    assert brd.game_over() == True

    brd.clear()

    # Anti-diagonal win
    brd.make_move("O", 2)
    brd.make_move("O", 4)
    brd.make_move("O", 6)
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    brd.clear()

    # Full board with no win
    moves = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    for i, move in enumerate(moves):
        brd.make_move(move, i)
    assert brd.has_won("X") == False
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    # Invalid move
    brd.make_move("X", 0)
    assert brd.make_move("O", 0) == False

    print("All tests passed!")

    # uncomment to play!
    play_tic_tac_toe()
