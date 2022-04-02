import constants
from game.casting.enemy import Enemy
from game.shared.point import Point
import random
import math

class Weapon(Enemy):
    def __init__(self, cast):
        super().__init__(cast)
        self.set_text(".")
        self.set_color(constants.YELLOW)
        self.set_font_size(15)
        x, y = self._get_player_pos()
        self.set_position(Point(x, y))
        self.set_velocity(self._set_initial_velocity())


    def move_next(self):
        try:
            x = (self._position.get_x() + self._velocity.get_x())
            y = (self._position.get_y() + self._velocity.get_y())
            if not 0 < x < constants.MAX_X or not 0 < y < constants.MAX_Y: # returns true if off screen
                self._cast.remove_actor("weapon", self)
            else:
                self.set_position(Point(x, y))
        except AttributeError: # If no active bullet on screen
            pass

    def _set_initial_velocity(self):
        enemy = self._choose_random_target()
        slope = self._make_vector(self._speed, enemy, shot=True)
        if slope != None:
            angle = math.atan(slope)
            x = math.cos(angle) * -self._direction_x(self.get_position().get_x(), enemy.get_position().get_x()) * self._speed
            y = math.sin(angle) * -self._direction_x(self.get_position().get_x(), enemy.get_position().get_x()) * self._speed
            return Point(x, y)
        else:
            x = 0
            y = self._speed * -self._verticial(self.get_position().get_y(), enemy.get_position().get_y())
            return Point(x, y)
            
    
    def _choose_random_target(self):
        """Returns an enemy to shoot at.
        """
        enemies = self._cast.get_actors("enemy")
        enemy = enemies[random.randint(0,len(enemies)-1)]
        return enemy
        
