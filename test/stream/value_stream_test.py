import random
from app.stream.value_stream import value_stream


def test_value_stream():
    x1 = random.uniform(0.0, 1.0)
    y1 = random.uniform(0.0, 1.0)
    z1 = random.uniform(0.0, 7.0)

    x2 = random.uniform(0.0, 1.0)
    y2 = random.uniform(0.0, 1.0)
    z2 = random.uniform(0.0, 7.0)

    vector1 = [x1, y1, z1]
    vector2 = [x2, y2, z2]

    result = value_stream(vector1, vector2)

    assert result <= 127
    assert result >= 0
