#!/usr/bin/env python3
# encoding: utf-8

import sys
import random


X = 2
Y = 2
num_of_mines = min(X, Y)


def pick_square():
    x_coord = input("type x coordinate between 0 and %s: " % (X - 1))
    y_coord = input("type y coordinate between 0 and %s: " % (Y - 1))
    try:
        x = int(x_coord)
        y = int(y_coord)
        if 0 <= int(x_coord) <= X and 0 <= int(y_coord) <= Y:
            return (x, y)
        else:
            print("Invalid coordinates. Try again.")
            pick_square()
    except:
        print("Couldn't validate coordinates, please try again.")
        pick_square()


class Board():

    def __init__(self):

        self.squares = [(x, y) for x in range(X) for y in range(Y)]
        self.visible_squares = []
        self.visible_show = {}
        # copy rather than "link" `squares` to avoid later annoyance
        self.hidden_squares = self.squares[:]
        self.mines = random.sample(self.squares, num_of_mines)

    def update(self, sq):
        # update hidden
        # update visible

        num_adj_mines = len(
            [pt for pt in self.neighbors(sq) if pt in self.mines])

        self.visible_show[sq] = num_adj_mines

        if sq in self.hidden_squares:
            self.hidden_squares.remove(sq)
        if sq not in self.visible_squares:
            self.visible_squares.append(sq)
        if num_adj_mines == 0:
            for neighbor in (set(self.hidden_squares) & set(self.neighbors(sq))):
                self.update(neighbor)

    def draw(self):
        # show hidden as '_'
        # show others as 3rd

        # delim to draw board as an actual 2D grid
        board_string_rep = ""
        # i start with y (columns) because it makes placing newlines easier
        for y in range(Y):
            for x in range(X):
                # draw sq
                if (x, y) in self.hidden_squares:
                    rep_char = '-'
                elif (x, y) in self.visible_squares:
                    if self.visible_show[(x, y)] == 0:
                        rep_char = '_'
                    else:
                        rep_char = str(self.visible_show[(x, y)])

                else:
                    print("error, shouldn't be possible")
                    sys.exit()
                board_string_rep += rep_char

                if x == (X - 1):
                    board_string_rep += "\n"

        print(board_string_rep)

    def neighbors(self, sq):
        """gets valid neighbors of a square """
        x, y = sq
        candidates = [(x + i, y + j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
        return [pt for pt in candidates if pt in self.squares]


def main():

    board = Board()

    # Initial picture so we can see what we're up against.
    board.draw()

    while True:
        choice = pick_square()

        if choice in board.mines:
            print("Sucks to be you. Game over.")
            break

        if set(board.hidden_squares) == set(board.mines):
            print("You win. Cue slow clap")
            break
        else:
            board.update(choice)
            if set(board.hidden_squares) == set(board.mines):
                print("You win. Cue slow clap")
                break
            board.draw()


if __name__ == '__main__':
    main()
