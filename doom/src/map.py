"""Map module for the game."""

import pygame as pg
from settings import TILE_SIZE

_ = False

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 1, _, _, _, 1, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Map:
    """Map class for the game."""

    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.tile_size = TILE_SIZE
        self.get_map()

        # Extra
        self.map_width = len(self.mini_map[0])
        self.map_height = len(self.mini_map)

    def get_map(self):
        """Generate the world map."""
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value == 1:
                    self.world_map[(i, j)] = value

    def draw(self):
        """Draw the map."""
        for pos in self.world_map:
            pg.draw.rect(
                self.game.screen,
                "darkgray",
                (pos[0] * self.tile_size, pos[1] * self.tile_size, self.tile_size, self.tile_size),
            )
