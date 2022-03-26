from game.casting.actor import Actor
from game.casting.player import Player
from game.shared.point import Point

import random
import constants

class Enemy(Actor):
    def __init__(self, cast):
        super().__init__()
        self._cast = cast
        self.set_text("*")
        self.set_color(constants.RED)
        x, y = self.__spawn_point()
        self.set_position(Point(x,y))
        self._speed = 2 # The rate at which x changes in pixels.

    def __spawn_point(self):
        """Makes sure that the enemy does not spawn too close to the player by a space of 900 pixels squared.
        """
        player_x, player_y = self.__get_player_pos()
        x = player_x
        y = player_y
        
        while abs(player_x - x) < 30 and abs(player_y - y) < 30:
            x = random.randint(0, constants.MAX_X)
            y = random.randint(0, constants.MAX_Y)

        return x, y
    
    def __get_player_pos(self):
        """Returns the x and y coordinate of the position of the player
        """
        player = self._cast.get_first_actor("player")
        x = player.get_position().get_x()
        y = player.get_position().get_y()
        return x, y

    def move_next(self):
        self._position = self._make_vector(self._speed)
        

    def _make_vector(self, speed):
        """
        Helper method used in move_next() - 
        Get player position and enemy position and find slope
        """

        def direction_x():
            if hero_x > enemy_x:
                return 1
            elif hero_x < enemy_x:
                return -1
            else:
                return 0

        def verticial():
            if hero_y > enemy_y:
                return 1
            elif hero_y < enemy_y:
                return -1
            else:
                return 0
        
        # def nerf(angle):
        #     if abs(angle) > 3:
        #         return angle / 3 
        #     else:
        #         return angle

        hero_x, hero_y = self.__get_player_pos()
        enemy_x = self.get_position().get_x()
        enemy_y = self.get_position().get_y()

        vector_angle = 1

        try:
            vector_angle = (hero_y - enemy_y) / (hero_x - enemy_x) # Formula for slope: (y2 - y1) / (x2 - x1)
          #  vector_angle = nerf(vector_angle)
            b = -(vector_angle * enemy_x - enemy_y)
            new_enemy_x = enemy_x + (speed * direction_x())
            new_enemy_y = int(vector_angle * new_enemy_x + b) # y = mx + b
        except ZeroDivisionError: # Vertical line
            new_enemy_x = enemy_x
            new_enemy_y = enemy_y + (speed * verticial())

        
        vector_point = Point(new_enemy_x, new_enemy_y)

        return vector_point
        
