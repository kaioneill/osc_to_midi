from app.util.vector_difference import vector_difference


class ValueStreamSum:

    def __init__(self):
        self.last_vector = [0.0, 0.0, 0.0]
        self.min_val = 20.0
        self.sum = 0.0

    def value_stream_sum(self, vector):
        difference = vector_difference(self.last_vector, vector)

        self.last_vector = vector

        # difference *= 10.0

        # val = (difference / weight) * 127
        val = difference * 50.0

        if difference < 0.003:
            self.sum = self.min_val
        else:
            self.sum += val

        self.sum = 127.0 if self.sum > 127.0 else self.sum
        self.sum = 0.0 if self.sum < 0.0 else self.sum
        return int(self.sum)
