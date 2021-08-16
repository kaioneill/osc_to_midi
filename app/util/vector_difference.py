def vector_difference(vector1, vector2):
    total = 0
    for i in range(3):
        total += abs(vector1[i] - vector2[i])

    return total
