import time
import mido
import app.constants.joint_map
from app.util.joint_handler import JointHandler
from app.util.note import Note

outport = mido.open_output()
joint_notes = app.constants.joint_map.JOINT_NOTES


class MidiNote:
    notes = []

    @classmethod
    def midi_note(cls, joint, user, vector):
        if joint in joint_notes.keys():
            joint_note = joint_notes[joint]
            note_velocity = JointHandler.midi_note(joint, vector)

            if note_velocity > 0.0:
                # if joint_note in cls.notes:
                #     Note(joint_note, note_velocity).stop_same_note()
                cls.notes.append(joint_note)
                cls.notes.remove(Note(joint_note, note_velocity).play_note())

            # if note_velocity > 0.0:
            #     outport.send(mido.Message(
            #         "note_on", note=joint_note, velocity=note_velocity))
            #     time.sleep(0.5)
            #     outport.send(mido.Message("note_off", note=joint_note))

            # if note_velocity > 0.0:
            #     outport.send(mido.Message(
            #         "note_on", note=joint_note, velocity=note_velocity))
            #     # time.sleep(0.2)

            # if note_velocity < 0.0:
            #     outport.send(mido.Message("note_off", note=joint_note))
