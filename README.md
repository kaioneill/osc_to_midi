# osc to midi

## overview

built to take in [OSCeleton](https://github.com/Sensebloom/OSCeleton) OSC messages from kinect skeleton tracking data and translate them into useful midi messages. The goal is to have a movement driven interactive instrument.

the goal is to use mostly TDD.

current status can be seen at [hikai.net](https://hikai.net/posts/kinect_instrument/).

## notes

run tests with `pytest -s`.

useful snippet similar enough to Ruby's 'binding.pry'.

```python
import code; code.interact(local=dict(globals(), **locals()))
```
