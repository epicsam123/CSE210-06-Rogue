from game.casting.actor import Actor
from game.shared.point import Point

class Time(Actor):
    def __init__(self, video_service):
        super().__init__()
        self._video_service = video_service
        self._time_delay = 0
        self.set_text(f"{self._video_service.get_time()}")

    def _set_time(self):
        return f"Seconds: {self._video_service.get_time() - self._time_delay}"

    def set_time_delay(self, time_delay):
        self._time_delay = time_delay

    def get_time(self):
        return int(self._video_service.get_time() - self._time_delay)
        
    def move_next(self):
        """Simply update the time
        """
        self.set_text(self._set_time())