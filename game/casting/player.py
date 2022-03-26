import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast
import pyray

class Player(Actor):
    """
    The hero of the game.
    """
    def __init__(self):
        super().__init__()
        self.set_position(Point(int(constants.MAX_X/2), int(constants.MAX_Y/2))) # Start the player in the middle of the screen
        self.set_text("#")
        self.set_color(constants.GREEN)