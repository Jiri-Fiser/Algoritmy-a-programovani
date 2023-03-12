from typing import Tuple, Union, Optional
from enum import Enum


class PColor(Enum):
    Black = 0
    White = 1


class MoveResult(Enum):
    OK = 0
    KO = 1
    RETAKE = 2


class Piece:
    def __init__(self, color:PColor):
        self._color = color
    @property
    def color(self) -> PColor:
        return self._color

    def __repr__(self) -> str:
        return f"Piece: [color={self.color}]"


class Field:
    def __init__(self, initial_stack=[]):
        #intial_stack = initial_stack is not None or []
        self._stack = []
        for piece in initial_stack:
            self.push_piece(piece)

    def push_piece(self, piece: Piece) -> None:
        if len(self) == 0 or piece.color == self.color:
           self._stack.append(piece)
        else:
            raise ValueError("Invalid color of piece")

    def test_pushing(self, color: PColor) -> MoveResult:
        if len(self) == 0 or color == self.color:
            return MoveResult.OK
        if len(self) == 1:
            return MoveResult.RETAKE
        return MoveResult.KO

    def pop_piece(self) -> Piece:
        assert len(self) > 0, "Pop from empty stack"
        return self._stack.pop()

    @property
    def color(self) -> Optional[PColor]:
        if len(self) == 0:
            return None
        return self._stack[0].color

    def __len__(self):
        return len(self._stack)

    def __repr__(self):
        return f"Field{self._stack}"


if __name__ == "__main__":
    lp = [Piece(PColor.White) for _ in range(5)]
    f = Field(lp)
    print(f)