import constants
from game.shared.point import Point
from game.casting.enemy import Enemy
import constants
from game.shared.point import Point
from game.casting.weapon import Weapon
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
        self.game_start = False
        
    def pre_start(self, cast, script):
        """Returns: True if space bar is hit.
        """
        self._dress_main_title(cast)

        menu = script.get_actions("input")[0]
        self._video_service.open_window()
        while self._video_service.is_window_open() and not menu.space_pressed:
            self._execute_actions("output", cast, script)
            self._execute_actions("input", cast, script)
        script.remove_action("input", menu)
        if not self._video_service.is_window_open():
            self._video_service.close_window()
        else:
            self.game_start = True

    def _dress_main_title(self, cast):
        menu = cast.get_all_actors()[1]
        menu.set_color(constants.RED)
        menu.set_position(Point(constants.MAX_X/2, constants.MAX_Y*.25))
        menu.set_font_size(30)
        menu.set_text("Rogue")

    def start_game(self, cast, script):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast class): The cast of actors.
            script (Script class): The script of actions.
        """
        time = cast.get_first_actor("time")
        time_delay = time.get_time()
        time.set_time_delay(time_delay)

        self._video_service.open_window()
        deploy_weapon = True
        while self._video_service.is_window_open():
            game_over = script.get_action("update", 1).is_game_over
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
            current_time = time.get_time()
            if current_time % 4 == 2 and deploy_weapon and not game_over: # Shoot every four seconds
                cast.add_actor("weapon", Weapon(cast))
                deploy_weapon = False
            if current_time % 2 == 1:
                deploy_weapon = True # Reload
            if current_time % 5 == 0 and self._count % 5 == 0 and current_time < 20:
                cast.add_actor("enemy", Enemy(cast))
            if current_time % 5 == 0 and self._count % 5 == 0 and current_time >= 20 and current_time < 40:
                cast.add_actor("enemy", Enemy(cast))
                cast.add_actor("enemy", Enemy(cast))
            if current_time % 5 == 0 and self._count % 5 == 0 and current_time >= 40:
                cast.add_actor("enemy", Enemy(cast))
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
