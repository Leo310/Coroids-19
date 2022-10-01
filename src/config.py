from enum import Enum


class GameConfig(Enum):
    SIZE = (1300, 750)


class PlayerConfig(Enum):
    SPEED = 300
    ROTATION_SPEED = 200


class ProjectileConfig(Enum):
    SPEED = 900
