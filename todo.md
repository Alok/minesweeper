Sort tuples only when they're put to screen

## errors

-   max recursion depth exceeded
    -   need to write iteratively
-   format string

``` {.python}
    board.update(choice)
  File "game.py", line 51, in update
    self.hidden_squares.remove(sq)
ValueError: list.remove(x): x not in list
```

-   \^ On squares called twice or with zero squares

## problem functions

update draw
