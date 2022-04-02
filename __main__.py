import constants
from game.casting.actor import Actor
from game.casting.blinking_space_intro import BlinkingSpaceIntro
from game.casting.cast import Cast
from game.casting.player import Player
from game.casting.enemy import Enemy  
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.control_menu_action import ControlMenuAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.casting.time import Time
from game.shared.point import Point


def main():
     
    # create the cast
    cast = Cast()
    cast.add_actor("menu", BlinkingSpaceIntro())
    cast.add_actor("menu", Actor())
    
    # start the game 
    keyboard_service = KeyboardService() 
    video_service = VideoService()
    director = Director(video_service)
  

    script = Script()
    script.add_action("input", ControlMenuAction (keyboard_service))
    script.add_action("output", DrawActorsAction(video_service, director))
    
    director.pre_start(cast, script)

    cast.add_actor("player", Player())
    cast.add_actor("enemy", Enemy(cast)) 
    cast.add_actor("time", Time(video_service))
    cast.add_actor("messages", Actor())
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    director.start_game(cast, script)


if __name__ == "__main__":
    main()