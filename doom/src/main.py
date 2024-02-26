"""Main module for the game."""

import sys

import pygame as pg
from map import Map
from player import Player
from raycasting import RayCasting
from settings import FPS, HEIGHT, WIDTH


class Game:
    """Main game class."""

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        """Start a new game."""
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)

    def update(self):
        """Update the game frame."""
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps() :.1f}")

    def draw(self):
        """Draw the game frame."""
        self.screen.fill("black")
        self.map.draw()
        self.player.draw()

    def check_events(self):
        """Check for events."""
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        """Main game loop."""
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
