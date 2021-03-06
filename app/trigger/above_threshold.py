from app.util.vector_difference import vector_difference


def above_threshold(vector1, vector2, threshold=0.03):
    max = 9.0

    val = 0.0

    difference = vector_difference(vector1, vector2)
    if difference >= threshold:
        # val = (difference - threshold) * (1 / (max - threshold))
        val = difference * 25.0

    return val
