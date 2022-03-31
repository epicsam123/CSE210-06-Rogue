import constants
import time
from game.scripting.action import Action
from game.shared.point import Point


class ControlMenuAction(Action):
    
    def __init__(self, keyboard_service) -> None:
        self._keyboard_service = keyboard_service
        self.space_pressed = False

    def execute(self, cast, script):
        """
        Returns: True if the game has begun
        """

        time_out = 0
        while True:
            if self._keyboard_service.is_key_down("space"):
                self.space_pressed = True
                break
            elif time_out > 500000:
                break
            else:
                time_out += 1
                continue

        space = cast.get_first_actor("menu")
        space.change_blink_state()
           

        
      