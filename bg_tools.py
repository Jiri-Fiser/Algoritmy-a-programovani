from typing import Tuple, Union, Optional
from random import randint


class DoubleDice:
    def __init__(self):
        pass

    def get_roll(self) -> Union[Tuple[int,int], Tuple[int,int,int,int]]:
        r1 = randint(1,6)
        r2 = randint(1,6)
        if r1 != r2:
            return r1, r2
        else:
            return r1, r1, r1, r1


if __name__ == "__main__":
    d = DoubleDice()
    for i in range(20):
        print(d.get_roll())

    p = Piece(PColor.Black)
    print(p.color)




