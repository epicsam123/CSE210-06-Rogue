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
        is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self.is_game_over = False
        self._winner = 0
        self._kills = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self.is_game_over:
            self._handle_player_collision(cast)
            self._handle_weapon_collision(cast)
            self._update_kill_count(cast)
            self._handle_game_over(cast, script)

    def _handle_player_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player = cast.get_first_actor("player")
        rect1 = player.create_rect(player)
        
        enemies = cast.get_actors("enemy")
        for enemy in enemies:
            rect2 = enemy.create_rect(enemy)
            if pyray.check_collision_recs(rect1,rect2):
                self.is_game_over = True

    def _handle_weapon_collision(self, cast):
        """Check to see if any of the enemies are hit by the bullet. If so, destroy enemy (remove its actor)
        """
        weapon = cast.get_actors("weapon")
        if len(weapon) > 0: # If a shot is on the screen.
            enemies = cast.get_actors("enemy")
            for bullet in weapon:
                rect1 = bullet.create_rect(bullet)
                for enemy in enemies:
                    rect2 = enemy.create_rect(enemy)
                    if pyray.check_collision_recs(rect1,rect2):
                        cast.remove_actor("enemy", enemy)
                        cast.remove_actor("weapon", bullet)
                        self._kills += 1
                        break

    def _update_kill_count(self, cast):
        kill_count = cast.get_first_actor("messages")
        kill_count.set_text(f"Enemies destroyed: {self._kills}")
        kill_count.set_position(Point(constants.MAX_X - 88, 0))


    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self.is_game_over:
            player = cast.get_first_actor("player")
            time = cast.get_first_actor("time")
            seconds_lasted = time.get_time()

            cast.remove_actor("time", time)
          
            # So the player cannot move anymore
            player.set_velocity(Point(0, 0))
            script.remove_action("input", script.get_action("input", 0))
        
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            message_position = Point(x, y)

            game_over_message = Actor()
            game_over_message.set_text("Game Over!")
            seconds_lasted_message = Actor()
            seconds_lasted_message.set_text(f"Lasted {seconds_lasted} Seconds")
            seconds_lasted_message.set_color(constants.YELLOW)
            game_over_message.set_position(message_position)
            cast.add_actor("messages", game_over_message)
            cast.add_actor("time", seconds_lasted_message)
            
            player.set_color(constants.WHITE)