
from decimal import DivisionByZero
from game.casting.actor import Actor
from game.casting.player import Player
from game.shared.point import Point
<<<<<<< HEAD
from game.casting.cast import Cast
=======
import random
import constants
>>>>>>> 505bd1e8523d7aa2a447ed8b369c72ccc14b8a1b

class Enemy(Actor):
    def __init__(self):
        super().__init__()
        self.set_text("*")
        self.set_color(constants.RED)
        x = random.randint(0,900)
        y = random.randint(0,450)  
        self.set_position(Point(x,y))

    
    def get_position(self):
        return super().get_position()

    def get_velocity(self):
        return super().get_velocity()
"""
    def move_next(self):
<<<<<<< HEAD
        player = cast.
        enemy = cast


        pass

    def _make_vector(self, player, enemy, speed):
        """
        Helper method used in move_next()
        """
=======
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
    def _make_vector(self, speed,cast):
>>>>>>> 505bd1e8523d7aa2a447ed8b369c72ccc14b8a1b
        # get player position and own position and find slope
        player = cast.get_first_actor("snakes").get_segments()[0]
        hero_x = player.get_position().get_x()
        hero_y = player.get_position().get_y()
        enemy_x = self.get_position().get_x()
        enemy_y = self.get_position().get_y()

        try:
            vector_angle = (hero_y - enemy_y) / (hero_x - enemy_x)
        except DivisionByZero:
            pass
        
        new_enemy_x = vector_angle * enemy_x
        new_enemy_y = vector_angle * enemy_y
        vector_point = Point(new_enemy_x, new_enemy_y)

        def direction_x(x):
            if hero_x > enemy_x:
                return x
            elif hero_x < enemy_x:
                return -x
            else:
                return 0

        return vector_point
        


"""













    