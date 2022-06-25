class SelectedPiece:
    def __init__(self):
        self._piece = None

    def is_set(self):
        return self._piece is not None

    def set(self, piece):
        self._piece = piece

    def reset(self):
        self._piece = None

    def __getattr__(self, item):
        return self._piece.__getattribute__(item)
