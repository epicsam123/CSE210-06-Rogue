
from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service, director):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._director = director

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._video_service.clear_buffer()

        if self._director.game_start:
            player = cast.get_first_actor("player")
            enemies = cast.get_actors("enemy")
            messages = cast.get_actors("messages")

            self._video_service.draw_actor(player)
            self._video_service.draw_actors(enemies)
            self._video_service.draw_actors(messages, True)
        
        else:
            menu = cast.get_actors("menu")
            self._video_service.draw_actors(menu, True)

        self._video_service.flush_buffer()