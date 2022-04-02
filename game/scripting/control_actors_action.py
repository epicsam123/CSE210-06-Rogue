import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the player.
    
    The responsibility of ControlActorsAction is to get the direction and move player accordingly.

    Attributes:
        _keyboard_service (KeyboardService class): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService class): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast class): The cast of Actors in the game.
            script (Script class): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('left'):
            if self._keyboard_service.is_key_down('up'):
                self._direction = Point(-10, -10) 
            elif self._keyboard_service.is_key_down('down'):
                self._direction = Point(-10,10)
            else:
                self._direction = Point(-10, 0)
        
        # right
        elif self._keyboard_service.is_key_down('right'):
            if self._keyboard_service.is_key_down('up'):
                self._direction = Point(10, -10) 
            elif self._keyboard_service.is_key_down('down'):
                self._direction = Point(10, 10)
            else:
                self._direction = Point(10, 0)

        # up
        elif self._keyboard_service.is_key_down('up'):
            if self._keyboard_service.is_key_down('right'):
                self._direction = Point(10, -10) 
            elif self._keyboard_service.is_key_down('left'):
                self._direction = Point(-10, -10)
            else:
                self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        elif self._keyboard_service.is_key_down('down'):
            if self._keyboard_service.is_key_down('right'):
                self._direction = Point(10, 10) 
            elif self._keyboard_service.is_key_down('left'):
                self._direction = Point(-10, 10)
            else:
                self._direction = Point(0,10)

        else: # No buttons pressed
            self._direction = Point(0, 0)

        player = cast.get_first_actor("player")
        player.set_velocity(self._direction)
       