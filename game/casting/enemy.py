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
        self._speed = 6 # The rate at which x changes in pixels.

    def __spawn_point(self):
        """Makes sure that the enemy does not spawn too close to the player by a space of 900 pixels squared.
        """
        player_x, player_y = self._get_player_pos()
        x = player_x
        y = player_y
        
        while abs(player_x - x) < 100 and abs(player_y - y) < 100:
            x = random.randint(0, constants.MAX_X)
            y = random.randint(0, constants.MAX_Y)

        return x, y
    
    def _get_player_pos(self):
        """Returns the x and y coordinate of the position of the player
        """
        player = self._cast.get_first_actor("player")
        x = player.get_position().get_x()
        y = player.get_position().get_y()
        return x, y

    def __get_enemy_pos(self, enemy):
        x = enemy.get_position().get_x()
        y = enemy.get_position().get_y()
        return x, y

    def move_next(self):
        self._position = self._make_vector(self._speed, self)

    def _direction_x(self, hero_x, enemy_x):
            if hero_x > enemy_x:
                return 1
            elif hero_x < enemy_x:
                return -1
            else:
                return 0

    def _verticial(self, hero_y, enemy_y):
            if hero_y > enemy_y:
                return 1
            elif hero_y < enemy_y:
                return -1
            else:
                return 0

    def _make_vector(self, speed, enemy, shot=False):
        """
        Helper method used in move_next() - 
        Get player position and enemy position and find slope
        """

        
        
        hero_x, hero_y = self._get_player_pos()
        enemy_x, enemy_y = self.__get_enemy_pos(enemy)


        try:
            vector_angle = (hero_y - enemy_y) / (hero_x - enemy_x) # Formula for slope: (y2 - y1) / (x2 - x1)
            b = enemy_y - vector_angle * enemy_x
            if shot:
                return vector_angle
            new_enemy_x = enemy_x + speed * self._direction_x(hero_x, enemy_x)
            if abs(enemy_x - hero_x) < speed:
                new_enemy_x = hero_x

            new_enemy_y = int(vector_angle * new_enemy_x + b) # y = mx + b
            if abs(enemy_y - new_enemy_y) > speed: 
                new_enemy_y = enemy_y + speed * self._verticial(hero_y, enemy_y) # nerf

        except ZeroDivisionError: # Vertical line
            if shot:
                return None
            new_enemy_x = enemy_x
            new_enemy_y = enemy_y + speed * self._verticial(hero_y, enemy_y)

        
        vector_point = Point(new_enemy_x, new_enemy_y)

        return vector_point
        
