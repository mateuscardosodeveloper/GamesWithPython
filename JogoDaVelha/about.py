"""
Umjogo da velha simples.

Licensa:

Copyright 2017 E.S Pereira
"""

from curses import initscr, wrapper

def about(StandardScren):
    StandardScren.clear()
    StandardScren.border()
    StandardScren.addstr(1, 1, "Pressione Q para sair ou H para exibir essa ajuda")
    StandardScren.addstr(2, 1, "Para mudar a posição, use as teclas: A, D, S, W")
    StandardScren.addstr(3, 1, "Para definir uma posição do jogo, digite: L")
    StandardScren.addstr(4, 1, "Para reuniciar a partida, digite: Y")
    StandardScren.addstr(5, 1, "Pressione espaço para sair dessa tela.")
    StandardScren.refresh()

def wellcome(StandardScren):
    StandardScren.addstr(1, 1, "Bem-vindo ao Jogo da Velha.")
    StandardScren.addstr(2, 1, "Presione q para sair ou h para pedir ajuda")
    