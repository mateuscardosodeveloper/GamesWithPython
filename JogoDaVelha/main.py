"""
Umjogo da velha simples.

Licensa:

Copyright 2017 E.S Pereira
"""

from curses import initscr, wrapper
from random import randint
from about import about, wellcome
from restart_screen import restart_screen
from board import board

       
def main(StandardScren):
    restart_screen(StandardScren)
    width = StandardScren.getmaxyx()[1]
    x_center = (width - 1) // 2
    posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    while True:
        entrada = StandardScren.getkey()
        if entrada == 'q':
            break
        if entrada == 'h':
            about(StandardScren)
        else:
            board(StandardScren, posicoes, x_center)


if __name__ == "__main__":
    initscr()
    wrapper(main)
