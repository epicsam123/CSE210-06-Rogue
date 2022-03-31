import constants
import time
import threading
import multiprocessing
from game.scripting.action import Action
from game.shared.point import Point


class ControlMenuAction(Action):
    
    def __init__(self, keyboard_service) -> None:
        self._keyboard_service = keyboard_service

    def execute(self, cast, script):
        """
        Returns: True if the game has begun
        """
        def time_out():
            time.sleep(0.01)
            return True


        def watch_space():
            
            from multiprocessing.pool import ThreadPool
            pool = ThreadPool(processes=1)

            async_result = pool.apply_async(count)
            async_result1 = pool.apply_async(space_pressed)
            # do some other stuff in the main process

            return_val = async_result.get()  # get the return value from your function.
            return_val1 = async_result1.get()

            def count():
                time.sleep(1)
                space = cast.get_first_actor("menu")
                space.change_blink_state()
                return True
            def space_pressed():
                while True: # Event listener
                    if self._keyboard_service.is_key_down("space"):
                        script.remove_action("input", script.get_action("input", 0))
                        return True
                    else:
                        continue
            time_out = False
            handle_blink = threading.Thread(target=count)
            handle_space = threading.Thread(target=space_pressed)
            handle_blink.start()
            handle_space.start()

            while True:
                if handle_space or handle_blink:
                    break
                else:
                    continue
            if space_pressed() or count():
                break
            handle_blink.start()
            
            return handle_space.start()

            

#          Another method, maybe??  
#  import concurrent.futures

# def foo(bar):
#     print('hello {}'.format(bar))
#     return 'foo'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future = executor.submit(foo, 'world!')
#     return_value = future.result()
#     print(return_value)

        # threads = []
        
        # threads.append(thread_1)
        # threads.append(thread_2)
        # for thread in threads:
        #     thread.join()

        