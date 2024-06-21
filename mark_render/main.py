from engine.geometry.basis import Basis
from engine.markengine import MarkEngine
from engine.mathmatic.vector2 import Vector2
from engine.mathmatic.vector3 import Vector3


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
engine = MarkEngine(800, 600)

v1 = Vector3(1, 0, 0)
v2 = Vector3(0, 1, 0)
v3 = Vector3(0, 0, 1)
c = 10

v1dotv1 = v1 * v1
v1dotv2 = v1 * v2
v1p = v1 * c
v1p = c * v1

basis = Basis(Vector2(1, 1), Vector2(-1, 1))
v2 = Vector2(1, 1)
v2p = basis.trasnform(v2)

if __name__ == '__main__':
    engine.loop()