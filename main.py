from game import Game
from console_ui import ConsoleUI


def main():
    game = Game()
    ui = ConsoleUI(game)
    ui.run()


if __name__ == '__main__':
    main()

