"""Player module for the game."""

import math

import pygame as pg
from settings import PLAYER_ANGLE, PLAYER_POS, PLAYER_RADIUS, PLAYER_ROT_SPEED, PLAYER_SPEED, WIDTH


class Player:
    """Player class for the game."""

    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.block = self.game.map.tile_size

    def movement(self):
        """Handle the player movement."""
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        """Check if there is a wall."""
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        """Check if there is a wall collision."""
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        """Draw the player."""
        # pg.draw.line(
        #     self.game.screen,
        #     "yellow",
        #     (self.x * self.block, self.y * self.block),
        #     (
        #         self.x * self.block + WIDTH * math.cos(self.angle),
        #         self.y * self.block + WIDTH * math.sin(self.angle),
        #     ),
        #     int(0.02 * self.block),
        # )

        pg.draw.circle(
            self.game.screen,
            "green",
            (self.x * self.block, self.y * self.block),
            PLAYER_RADIUS * self.block,
        )

    def update(self):
        """Update the player."""
        self.movement()

    @property
    def pos(self):
        """Return the player position."""
        return self.x, self.y

    @property
    def map_pos(self):
        """Return the player position on the mini map."""
        return int(self.x), int(self.y)
