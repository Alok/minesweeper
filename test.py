import game


board = game.Board()

def test_board():
    assert len(board.squares) == game.X * game.Y
