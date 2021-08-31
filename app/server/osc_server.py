import argparse
import time
import mido
from pythonosc import dispatcher
from pythonosc import osc_server

from app.stream.value_stream import value_stream
from app.trigger.many_above_trigger import ManyAboveTrigger

# inport = mido.open_input()
outport = mido.open_output()
# outport.send(mido.Message("note_off", note=joint_note))

joint_cc_map = {
    "l_hand": 17
}

joint_note = 60

history = {}
history_trigger = {}
paused = False

for joint in joint_cc_map:
    history[joint] = [0.0, 0.0, 0.0]
    history_trigger[joint] = [0.0, 0.0, 0.0]


def print_joint(unused_addr, joint, user, x, y, z):
    print("{} {} {} {} {}".format(joint, user, x, y, z))


def cc_stream(unused_addr, joint, user, x, y, z):
    global joint_cc_map
    global joint_note
    global history
    if joint in joint_cc_map:
        val = value_stream(history[joint], [x, y, z])

        cc = joint_cc_map[joint]
        outport.send(mido.Message("control_change", control=cc, value=val))

        history[joint] = [x, y, z]


def note_trigger(unused_addr, joint, user, x, y, z):
    global joint_cc_map
    global joint_note
    global history_trigger
    global paused

    if not paused:
        if joint in joint_cc_map:
            note_velocity = ManyAboveTrigger().many_above_trigger(
                history_trigger[joint], [x, y, z])

            if note_velocity > 0.0:
                outport.send(mido.Message("note_on", note=joint_note))
                paused = True
                pause()

                time.sleep(0.2)
                outport.send(mido.Message("note_off", note=joint_note))

    history_trigger[joint] = [x, y, z]


def pause():
    global paused

    time.sleep(0.1)
    paused = False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="192.168.10.200", help="The ip to listen on")
    parser.add_argument("--port",
                        type=int, default=7110, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    # dispatcher.map("/joint", print_joint)
    dispatcher.map("/joint", cc_stream)

    dispatcher.map("/joint", note_trigger)

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
    # print("Serving on {}".format(server.server_address))
    server.serve_forever()
