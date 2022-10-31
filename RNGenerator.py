import math

class RNGererator:
    __a: int = 1_664_525
    __c: int = 1_013_904_223
    __m: int = math.pow(2, 32)

    def __init__(self, seed: int = 0) -> None:
        self.__seed = seed

    def __next_seed(self, Z: int) -> int:
        self.__seed = (self.__a * Z + self.__c) % self.__m
    
    def next_random(self) -> float:
        self.__next_seed(self.__seed)
        return self.__seed / self.__m
