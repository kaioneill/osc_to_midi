from unittest.mock import patch
from app.util.message_handler import message_handler


@patch("app.util.message_handler.midi_cc")
@patch("app.util.message_handler.midi_note")
def test_message_handler(self, patch_cc, patch_note):
    unused_addr = None
    joint = "r_hand"
    user = 1
    x = 0.523
    y = 0.345
    z = 2.567

    message_handler(unused_addr, joint, user, x, y, z)

    assert patch_cc.called
    assert patch_note.called
