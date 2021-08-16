from noise import pnoise1


def vector_stream(length=100):
    x = pnoise1
    y = pnoise1
    z = pnoise1
    stream = []

    step = 0.0
    for i in range(length):
        step += 1 / float(length)
        stream.append(
            [
                normalize1(x(step)),
                normalize1(y(step)),
                normalize7(z(step))
            ])

    return stream


# takes value -1..1 and converts to 0..1
def normalize1(val):
    return (val + 1) * 0.5


# takes value -1..1 and converts to 0..7
def normalize7(val):
    return (val + 1) * (7 / 2.0)
