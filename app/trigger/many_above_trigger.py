import time
from app.trigger.above_threshold import above_threshold


class ManyAboveTrigger:
    # last_vector = [0.0, 0.0, 0.0]
    min_velocity = 20.0

    def many_above_trigger(self, last_vector, vector):
        val = above_threshold(last_vector, vector)
        # self.last_vector = vector

        if val > 0.0:
            val *= 127.0
            val += self.min_velocity
            val = 127.0 if val > 127.0 else val

        return int(val)
