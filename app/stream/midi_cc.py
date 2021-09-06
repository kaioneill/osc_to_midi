import mido
import app.constants.joint_map
from app.util.joint_handler import JointHandler

outport = mido.open_output()
joint_ccs = app.constants.joint_map.JOINT_CCS


def midi_cc(joint, user, vector):
    if joint in joint_ccs.keys():
        joint_cc = joint_ccs[joint]["cc"]
        cc_val = JointHandler.midi_cc(joint, vector)

        outport.send(mido.Message("control_change",
                                  control=joint_cc, value=cc_val))
