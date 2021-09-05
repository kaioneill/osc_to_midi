import time
import mido

outport = mido.open_output()


class Note:
    def __init__(self, note_number, velocity):
        self.note_number = note_number
        self.velocity = velocity

    def play_note(self):
        outport.send(mido.Message(
            "note_on", note=self.note_number, velocity=self.velocity))
        time.sleep(0.7)
        outport.send(mido.Message("note_off", note=self.note_number))
        return self.note_number

    def stop_same_note(self, note_number):
        outport.send(mido.Message("note_off", note=self.note_number))
