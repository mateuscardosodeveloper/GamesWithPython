"""
Umjogo da velha simples.

Licensa:

Copyright 2017 E.S Pereira
"""
from about import wellcome
 
def restart_screen(StandardScren, clean = True):
    if clean is True:
        StandardScren.clear()
    StandardScren.border()
    wellcome(StandardScren)
    StandardScren.refresh()