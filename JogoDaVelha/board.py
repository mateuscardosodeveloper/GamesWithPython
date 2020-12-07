"""
Umjogo da velha simples.

Licensa:

Copyright 2017 E.S Pereira
"""

from curses import initscr
from restart_screen import restart_screen

def board(StandardScreen, posicoes, x_center):
    StandardScreen.clear()
    restart_screen(StandardScreen, clean=False)

    StandardScreen.addstr(10, x_center - 3, "------")
    StandardScreen.addstr(12, x_center - 3, "------")
    i=9
    for linha in posicoes:
        tela = "%s|%s|%s" % tuple(linha)
        StandardScreen.addstr(i, x_center - 3, tela)
        i = i + 2
 