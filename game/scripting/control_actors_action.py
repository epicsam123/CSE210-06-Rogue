import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('a'):
            if self._keyboard_service.is_key_down('w'):
                self._direction = Point(-10, -10) 
            elif self._keyboard_service.is_key_down('s'):
                self._direction = Point(-10,10)
            else:
                self._direction = Point(-10, 0)
        
        # right
        elif self._keyboard_service.is_key_down('d'):
            if self._keyboard_service.is_key_down('w'):
                self._direction = Point(10, -10) 
            elif self._keyboard_service.is_key_down('s'):
                self._direction = Point(10, 10)
            else:
                self._direction = Point(10, 0)

        # up
        elif self._keyboard_service.is_key_down('w'):
            if self._keyboard_service.is_key_down('d'):
                self._direction = Point(10, -10) 
            elif self._keyboard_service.is_key_down('a'):
                self._direction = Point(-10, -10)
            else:
                self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        elif self._keyboard_service.is_key_down('s'):
            if self._keyboard_service.is_key_down('d'):
                self._direction = Point(10, 10) 
            elif self._keyboard_service.is_key_down('a'):
                self._direction = Point(-10, 10)
            else:
                self._direction = Point(0,10)

        else: # No buttons pressed
            self._direction = Point(0, 0)
        snake = cast.get_first_actor("player")
        snake.turn_head(self._direction)
       