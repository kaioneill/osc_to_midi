from app.trigger.above_threshold import above_threshold
from app.util.vector_difference import vector_difference


class ManyAboveTrigger:

    def __init__(self):
        self.last_vector = [0.0, 0.0, 0.0]
        self.min_velocity = 20.0
        self.paused = False

    def many_above_trigger(self, vector):
        if not self.paused:
            val = above_threshold(self.last_vector, vector)
            self.last_vector = vector

            if val > 0.0:
                self.paused = True
                val *= 127.0
                val += self.min_velocity
                val = 127.0 if val > 127.0 else val

            return int(val)
        else:
            difference = vector_difference(self.last_vector, vector)

            if difference < 0.03:
                self.paused = False

            self.last_vector = vector

            return 0
