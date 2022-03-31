import constants
from game.shared.point import Point
from game.casting.enemy import Enemy
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play, 
    such as deciding when enemies spawn.

    Attributes:
        _video_service (VideoService class): For providing video output.
    """

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService class): An instance of VideoService.
        """
        self._video_service = video_service
        self._count = 0 # Num enemies
        

    
    
    def start_game(self, cast, script):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast class): The cast of actors.
            script (Script class): The script of actions.
        """

        self._video_service.open_window()
        start_message = Actor()
        start_message.set_text("Press Space to start")
        start_message.set_position(Point(constants.MAX_X/2, constants.MAX_Y/2))
        cast.add_actor("menu", start_message)
        draw_space = script.get_actions('input')[0]
        player.set_color(constants.WHITE)
        cast.add_actor("player", Player())
        cast.add_actor("enemy", Enemy(cast))    
        
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            if space_pressed:
                self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
            if int(self._video_service.get_time()) % 5 == 0 and self._count % 5 == 0 and int(self._video_service.get_time()) < 20:
                cast.add_actor("enemy", Enemy(cast))
            if int(self._video_service.get_time()) % 5 == 0 and self._count % 5 == 0 and int(self._video_service.get_time()) >= 20:
                cast.add_actor("enemy", Enemy(cast))
                cast.add_actor("enemy", Enemy(cast))
            self._count += 1 
        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(cast, script)  
