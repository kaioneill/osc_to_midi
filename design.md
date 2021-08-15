# OSC Interpreter Design

## Goal

I want to get the osc data into a usable format. This really means getting the "shape" out of it, interpreting the form of the data stream per joint and the body as a whole into meaningful MIDI output.

### What is meaningful?

I want to determine what movements or combination of movements are worth doing something with on the output side.

- The first clear thing that seems worth including is large/fast (both?) gestures by a single joint like a hand wave or a kick.
- Additionally and separately trackable would be multiple large/fast movements at once.
- Slow and continuous movements would be nice to keep track of to allow for gradual change.

All of the above should be trackable on distinct axes and as a combined measure on multiple axes.

## Implementation concerns

### Data summing

There seems to be a theme of wanting discrete and combined measures for both joints and axes. The first concern this brings up is whether to combine measurements in the OSC interpreting code or leave that all to the MIDI consumer, broadcasting data on separate streams for all joint/axis combinations.

### Triggers vs streams

Some events, like a hand wave or kick (any fast gesture), should be able to be treated as a single trigger event (note on or similar) to allow for one off effects. Other movements, gradual crouching or standing (any slow movement), should output a stream of gradually changing data.

It seems that the data for these two scenarios would need to be processed in parallel (not true parallel) to allow for a single joint to output both trigger and stream data.

## Basic units of function

### OSC parsing and object model

- A format to hold joint and axis data
- Mechanism to get OSC data into that format

### Joint routing

- Take formatted data and do something with it?

### Axis scale normalization

- Z axis scale is different
- Scale ranges to useful values
- Perhaps some sort of vector approach

### Robust MIDI output value scaling/weighting

- All output values within MIDI range
- Joints/channels may require different scalars 

### Trigger capturing

- Capture fast joint movements over two or more frames
- Emit a single event (with a relative intensity?)

### Joint and axis summing

- Multi joint/axis gestures do something special

### MIDI channel and event mapping

- Flexible output options for channel and event mappings

### Noise filtering

- Small movements and noise upstream should not affect output

## Other thoughts

### Vectors

Perhaps some vector based approach using offsets between frames of the same joint, especially useful for speed based trigger events.

### OSC stream

Separate out any MIDI concerns, the real work is done in a system that outputs an OSC stream.

sample messages with stream (gradual) and trigger (fast) events
```
stream l_hand 0.523
stream l_hand 0.531
trigger r_hand 0.844
stream l_hand 0.517
```