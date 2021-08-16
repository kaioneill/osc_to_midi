from app.util.vector_difference import vector_difference


def value_stream(vector1, vector2):
    weight = 10

    difference = vector_difference(vector1, vector2)

    val = (difference / weight) * 127

    val = 127 if val > 127 else val
    return val
