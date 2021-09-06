from app.util.vector_difference import vector_difference


class ValueStreamSum:

    def __init__(self, range=(20, 127)):
        self.last_vector = [0.0, 0.0, 0.0]
        self.sum = range[0]
        self.range = range

    def value_stream_sum(self, vector):
        difference = vector_difference(self.last_vector, vector)

        self.last_vector = vector

        # difference *= 10.0

        # val = (difference / weight) * 127
        val = difference * 50.0

        if difference < 0.01:
            self.sum -= (difference) * 200.0
        else:
            self.sum += val

        self.sum = self.range[1] if self.sum > self.range[1] else self.sum
        self.sum = self.range[0] if self.sum < self.range[0] else self.sum
        return int(self.sum)
