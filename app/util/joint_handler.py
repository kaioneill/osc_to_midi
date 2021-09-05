import app.constants.joint_map
# from app.stream.value_stream import ValueStream
from app.stream.value_stream_sum import ValueStreamSum
from app.trigger.many_above_trigger import ManyAboveTrigger


class JointHandler:
    joint_notes = app.constants.joint_map.JOINT_NOTES
    joint_ccs = app.constants.joint_map.JOINT_CCS

    triggers = {}
    streams = {}

    for joint in joint_notes:
        triggers[joint] = ManyAboveTrigger()

    for joint in joint_ccs:
        # streams[joint] = ValueStream()
        streams[joint] = ValueStreamSum()

    @classmethod
    def midi_note(cls, joint, vector):
        if joint in cls.joint_notes.keys():
            return cls.triggers[joint].many_above_trigger(vector)

    @classmethod
    def midi_cc(cls, joint, vector):
        if joint in cls.joint_ccs.keys():
            # return cls.streams[joint].value_stream(vector)
            return cls.streams[joint].value_stream_sum(vector)
