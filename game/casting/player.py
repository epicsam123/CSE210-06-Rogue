from decimal import MAX_EMAX
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast
import pyray

class Player(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        for segment in self._segments:
            segment.move_next()
    def get_head(self):
        return self._segments[0]

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def create_rect(self,object):
        return pyray.Rectangle(object.get_position().get_x(),object.get_position().get_y(),10,10)

    def _prepare_body(self):
        x = 450
        y = 300
        position = Point(x * constants.CELL_SIZE, y)
        velocity = Point(1 * constants.CELL_SIZE, 0)
        segment = Actor()
        segment.set_text("#")
        segment.set_color(constants.GREEN)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)