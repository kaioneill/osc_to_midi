from app.util.vector_difference import vector_difference


class ValueStream:

    def __init__(self):
        self.last_vector = [0.0, 0.0, 0.0]
        self.min_val = 20.0

    def value_stream(self, vector):
        weight = 3

        difference = vector_difference(self.last_vector, vector)
        self.last_vector = vector

        difference *= 10.0

        # val = (difference / weight) * 127
        val = difference * 127.0

        val += self.min_val

        val = 127.0 if val > 127.0 else val
        return int(val)
