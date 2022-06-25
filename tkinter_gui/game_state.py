from game import Game


class GameState:

    def __init__(self, game: Game):
        self._game = game

    @property
    def current_player(self):
        return self._game.current_player.name.lower()

    @property
    def current_player_is_in_check(self):
        return self._game.current_player_is_in_check()

