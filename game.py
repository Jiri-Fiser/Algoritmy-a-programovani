from typing import List, Tuple, Optional, Sequence
from enum import Enum
from random import randrange

from piece import PColor, Piece, Field

class GameState(Enum):
    ON_MOVE = 0
    END_ROUND = 1
    END_GAME_1 = 2
    END_GAME_2 = 3
    END_GAME_3 = 4


class MoveResult(Enum):
    INVALID = 0
    VALID = 1
    VALID_RETAKE = 2
    VALID_OUT = 3


class Move:
    def __init__(self, start_field, end_field):
        pass
    def __len__(self):
        pass
    def __repr__(self):
        pass


class Game:
    def __init__(self):
        self.bar = {PColor.White: 0, PColor.Black: 0}
        self.bank = {PColor.White: 0, PColor.Black: 0}
        self.fields = [Field() for _ in range(24)]
        self.color = PColor.White if randrange(2) else PColor.Black
        self.pieces = []

    def load_from_json(self, json_object):
        pass

    def startPosition(self):
        pass

    @property
    def player_color(self):
        pass

    @property
    def dice(self):
        pass

    def start_round(self):
        pass

    @property
    def state(self) -> GameState:
        pass

    def get_moves(self) -> List[Move]:
        pass

    def play(self, move: Move) -> MoveResult:
        pass

    @property
    def bar(self) -> Tuple[int, int]: # počet bílých a černých na baru
        pass

    def bank(self) -> Tuple[int, int]:
        pass

    @property
    def field(self) -> Tuple[Optional[PColor], int]:
        pass

    def all_pieces(self) -> Sequence[Piece]:
        pass
