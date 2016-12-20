# draw chars




class Board(object):

    hidden_char = '_'
    visible_char = ' '

    """X: width, Y: height"""

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        # *should* be sorted lexicograpically by default
        self.squares = [(x, y) for x in range(X) for y in range(Y)]



    self.grid = 
    visible_squares = []
    hidden_squares = self.squares

    def draw()
        for square in self.squares:
            if square in hidden_squares:
