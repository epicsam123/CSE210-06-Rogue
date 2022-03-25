from decimal import DivisionByZero
from game.casting.actor import Actor
from game.casting.player import Player
from game.shared.point import Point
from game.casting.cast import Cast

class Enemy(Actor):
    def __init__(self):
        super().__init__()

    

    
    def get_position(self):
        return super().get_position()

    def get_velocity(self):
        return super().get_velocity()
    
    def move_next(self):
        player = cast.
        enemy = cast


        pass

    def _make_vector(self, player, enemy, speed):
        """
        Helper method used in move_next()
        """
        # get player position and own position and find slope
        hero_x = player.get_position().get_x()
        hero_y = player.get_position().get_y()
        enemy_x = enemy.get_position().get_x()
        enemy_y = enemy.get_position().get_y()

        try:
            vector_angle = (hero_y - enemy_y) / (hero_x - enemy_x)
        except DivisionByZero:
            pass
        
        new_enemy_x = vector_angle * enemy_x

        vector_point = Point(new_enemy_x, new_enemy_y)

        def direction_x(x):
            if hero_x > enemy_x:
                return x
            elif hero_x < enemy_x:
                return -x
            else:
                return 0

        return vector_point
        









    