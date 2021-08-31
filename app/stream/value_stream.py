from app.util.vector_difference import vector_difference


def value_stream(vector1, vector2):
    weight = 3

    difference = vector_difference(vector1, vector2)

    difference *= 10.0

    # val = (difference / weight) * 127
    val = difference * 127.0

    val = 127.0 if val > 127.0 else val
    return int(val)
