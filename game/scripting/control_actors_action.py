import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    INHERITS ACTION, ONE INSTANCE OF POLYMORPHISM

    An input action that controls the player.

    Supports diagonal movements.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
        _direction: direction of player (velocity is 0 as default)
        
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, 0)

    def execute(self, cast, script): # Polymorphism
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('left'):
            if self._keyboard_service.is_key_down('up'):
                self._direction = Point(-constants.CELL_SIZE, -constants.CELL_SIZE) 
            elif self._keyboard_service.is_key_down('down'):
                self._direction = Point(-constants.CELL_SIZE, constants.CELL_SIZE)
            else:
                self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        elif self._keyboard_service.is_key_down('right'):
            if self._keyboard_service.is_key_down('up'):
                self._direction = Point(constants.CELL_SIZE, -constants.CELL_SIZE) 
            elif self._keyboard_service.is_key_down('down'):
                self._direction = Point(constants.CELL_SIZE, constants.CELL_SIZE)
            else:
                self._direction = Point(constants.CELL_SIZE, 0)

        # up
        elif self._keyboard_service.is_key_down('up'):
            if self._keyboard_service.is_key_down('right'):
                self._direction = Point(constants.CELL_SIZE, -constants.CELL_SIZE) 
            elif self._keyboard_service.is_key_down('left'):
                self._direction = Point(-constants.CELL_SIZE, -constants.CELL_SIZE)
            else:
                self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        elif self._keyboard_service.is_key_down('down'):
            if self._keyboard_service.is_key_down('right'):
                self._direction = Point(constants.CELL_SIZE, constants.CELL_SIZE) 
            elif self._keyboard_service.is_key_down('left'):
                self._direction = Point(-constants.CELL_SIZE, constants.CELL_SIZE)
            else:
                self._direction = Point(0, constants.CELL_SIZE)

        else: # No buttons pressed
            self._direction = Point(0, 0)
        
        player = cast.get_first_actor("player")
        player.move_next(self._direction)