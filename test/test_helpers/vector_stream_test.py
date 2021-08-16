from test.test_helpers.vector_stream import vector_stream


def test_vector_stream():
    result = vector_stream()

    assert len(result) == 100
    assert all(
        map(
            lambda x: x[0] > 0.0 and x[0] < 1.0, result
        )
    )
    assert all(
        map(
            lambda x: x[1] > 0.0 and x[1] < 1.0, result
        )
    )
    assert all(
        map(
            lambda x: x[2] > 0.0 and x[2] < 7.0, result
        )
    )
