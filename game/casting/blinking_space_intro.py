from matplotlib.pyplot import show
from game.casting.actor import Actor
from game.shared.point import Point
import constants

class BlinkingSpaceIntro(Actor):
    def __init__(self):
        super().__init__()
        self._showing = True
        self._text = "Hold Space to start"
        self.set_color(constants.GREEN)
        self.set_position(Point(constants.MAX_X/2, constants.MAX_Y*.75))
    
    def change_blink_state(self):
        def show_text():
            if self._showing:
                self._text = "Hold Space to start"
            else:
                self._text = ""

        self._showing = not self._showing
        show_text()
        

    

    