import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
import pyray

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_player_collision(cast)
            self._handle_game_over(cast, script)

    def _handle_player_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player = cast.get_first_actor("player")
        enemies = cast.get_actors("enemy")

        for enemy in enemies:
            rect1 = player.create_rect(player)
            rect2 = enemy.create_rect(enemy)
            if pyray.check_collision_recs(rect1,rect2):
                self._is_game_over = True

    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player = cast.get_first_actor("player")
          
            # So the player cannot move anymore
            player.set_velocity(Point(0, 0))
            script.remove_action("input", script.get_action("input", 0))
        
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            message_position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(message_position)
            cast.add_actor("messages", message)
            
            player.set_color(constants.WHITE)