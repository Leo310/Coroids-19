from enum import Enum


class GameConfig(Enum):
    SIZE = (1300, 750)


class PlayerConfig(Enum):
    SPEED = 300
    ROTATION_SPEED = 200
    SIZE = (100, 100)
    IMMUNITY = 1.5


class ProjectileConfig(Enum):
    SPEED = 900
    SIZE = (60, 38)


class EnemyConfig(Enum):
    SIZE = (100, 100)


class MenuConfig(Enum):
    TEXT_COLOR = "#018CF3"
