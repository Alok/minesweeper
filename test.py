import game


def test_board():
    assert len(game.board.squares) == game.board.width * game.board.height
