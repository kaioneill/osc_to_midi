import time
from app.trigger.above_threshold import above_threshold


class ManyAboveTrigger:
    last_vector = [0.0, 0.0, 0.0]

    def many_above_trigger(self, vector):
        val = above_threshold(self.last_vector, vector)
        self.last_vector = vector
        time.sleep(0.1)
        return val
