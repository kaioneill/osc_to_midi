from test.test_helpers.vector_stream import vector_stream
from app.trigger.many_above_trigger import ManyAboveTrigger


def test_many_above_trigger():
    vals = []
    for vector in vector_stream()[:20]:
        vals.append(ManyAboveTrigger().many_above_trigger(vector))

    assert any(
        map(
            lambda x: x == 0.0, vals
        )
    )
    assert any(
        map(
            lambda x: x > 0.0, vals
        )
    )
