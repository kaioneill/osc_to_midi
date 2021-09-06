from app.util.vector_difference import vector_difference


class ValueStream:

    def __init__(self, range=(20, 127)):
        self.last_vector = [0.0, 0.0, 0.0]
        self.range = range

    def value_stream(self, vector):
        difference = vector_difference(self.last_vector, vector)
        self.last_vector = vector

        difference *= 10.0

        # val = (difference / weight) * 127
        val = difference * 127.0

        val = self.range[1] if val > self.range[1] else val
        val = self.range[0] if val < self.range[0] else val
        return int(val)
