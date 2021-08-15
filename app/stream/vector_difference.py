def vector_difference(vector1, vector2):
    weight = 10

    total = 0
    for i in range(3):
        total += abs(vector1[i] - vector2[i])

    val = (total / weight) * 127

    val = 127 if val > 127 else val
    return val
