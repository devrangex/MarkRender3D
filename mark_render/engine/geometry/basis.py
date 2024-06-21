from engine.mathmatic.vector2 import Vector2

""" 기저 벡터 """
class Basis:
    def __init__(self, basis1: Vector2 = Vector2(1, 0), basis2: Vector2 = Vector2(0, 1)) -> None:
        self.__basis1 = basis1
        self.__basis2 = basis2
        
    def trasnform(self, input) -> Vector2:
        # linear combination
        # | b1.x    b2.x | | x | = | x' |
        # | b1.y    b2.y | | y |   | y' |
        #
        # x * b1 + y * b2 = x'
        #
        # x * b1
        return (input.x * self.__basis1) + (input.y * self.__basis2)