import sys
from game import Game

from tkinter_gui import TkInterGUI


def main():
    gui = TkInterGUI(Game())
    gui.run()


if __name__ == '__main__':
    sys.exit(main())

