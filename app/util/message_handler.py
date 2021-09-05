from app.stream.midi_cc import midi_cc
from app.trigger.midi_note import MidiNote


def message_handler(unused_addr, joint, user, x, y, z):
    vector = [x, y, z]

    midi_cc(joint, user, vector)
    MidiNote.midi_note(joint, user, vector)
