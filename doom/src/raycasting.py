"""Raycasting module for the game."""

import math

import pygame as pg
from settings import DELTA_ANGLE, HALF_FOV, MAX_DEPTH, NUM_RAYS, PLAYER_RADIUS, TILE_SIZE


class RayCasting:
    """Ray casting class for the game."""

    def __init__(self, game):
        self.game = game
        self.block = self.game.map.tile_size
        # self.texture = pg.image.load("assets/wall.jpg").convert()
        # self.texture = pg.transform.scale(self.texture, (self.block, self.block // 2))

    def ray_cast(self):
        """Ray casting algorithm."""
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for _ in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for _ in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for _ in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            depth, offset = (depth_vert, y_vert) if depth_vert < depth_hor else (depth_hor, x_hor)
            # texture = int(x_vert) % self.block

            if abs(depth) >= PLAYER_RADIUS:

                start_ray = (ox + PLAYER_RADIUS * cos_a) * self.block, (oy + PLAYER_RADIUS * sin_a) * self.block
                end_ray = (ox + depth * cos_a) * self.block, (oy + depth * sin_a) * self.block

                pg.draw.line(
                    self.game.screen,
                    "yellow",
                    start_ray,
                    end_ray,
                    int(0.02 * self.game.map.tile_size),
                )

            ray_angle += DELTA_ANGLE

    def update(self):
        """Update the ray casting."""
        self.ray_cast()

    # def draw(self):
    #     ox, oy = self.game.player.pos
