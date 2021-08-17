from app.trigger.above_threshold import above_threshold


def test_above_threshold_max():
    x1 = 0.0
    y1 = 0.0
    z1 = 0.0

    x2 = 1.0
    y2 = 1.0
    z2 = 7.0

    vector1 = [x1, y1, z1]
    vector2 = [x2, y2, z2]

    result = above_threshold(vector1, vector2)

    assert result == 1.0


def test_above_threshold_min():
    x1 = 0.0
    y1 = 0.0
    z1 = 0.0

    x2 = 0.0
    y2 = 0.0
    z2 = 0.0

    vector1 = [x1, y1, z1]
    vector2 = [x2, y2, z2]

    result = above_threshold(vector1, vector2)

    assert result == 0.0
