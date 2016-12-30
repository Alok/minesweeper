#!/usr/bin/env python3
# encoding: utf-8

import sys
import random
import os
import urwid

sys.setrecursionlimit(10000)

X = 5
Y = 5
num_of_mines = min(X,Y)

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
    def __init__(self, X, Y):
        self.width = X
        self.height = Y

        self.squares = [(x, y) for x in range(self.width)
                        for y in range(self.height)]
        self.visible_squares = []
        self.visible_show = {}
        # copy rather than "link" `squares` to avoid later annoyance
        self.hidden_squares = self.squares[:]
        self.mines = random.sample(self.squares, num_of_mines)

    def update(self, sq):
        # add check that square exists in hidden or visible
        # change visible squares, set hidden to complement
        to_be_revealed = []

        num_adj_mines = len(
            [pt for pt in self.neighbors(sq) if pt in self.mines])

        if num_adj_mines >= 1:
            if sq in self.hidden_squares:
                # remove from hidden
                self.hidden_squares.remove(sq)
            # move that point to visible
            self.visible_squares.append(sq)
            self.visible_show[sq] = num_adj_mines
        else:
            for neighbor in self.neighbors(sq):
                self.update(neighbor)
                if sq in self.hidden_squares:
                    self.hidden_squares.remove(sq)

    def draw(self):
        # show hidden as '_'
        # show others as 3rd


        # delim to draw board as an actual 2D grid
        board_string_rep = ""
        for sq in self.squares:
            delim = '\n' if sq[0] == X - 1 else ''

            if sq in self.hidden_squares:
                board_string_rep += '_' + delim
            elif sq in self.visible_squares:
                if self.visible_show[sq] == 0:
                    board_string_rep += ' ' + delim
                else:
                    board_string_rep += ('%s' %
                                         (self.visible_show[sq])) + delim
            else:
                print("error, shouldn't be possible")
                sys.exit()

        print(board_string_rep)


    def neighbors(self, sq):
        """gets valid neighbors of a square """
        x, y = sq
        candidates = [(x + i, y + j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
        return [pt for pt in candidates if pt in self.squares]



def main():

    board = Board(X, Y)
    print(board.mines)

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
