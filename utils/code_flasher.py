"""
from usys import stdin, stdout
from uselect import poll
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

motor = Motor(Port.A)

keyboard = poll()
keyboard.register(stdin)

while True:
    while not keyboard.poll(0):
        wait(10)
    cmd = stdin.buffer.read(3)   # e.g. fixed-size 3-byte commands
    if cmd == b"fwd":
        motor.dc(50)
    elif cmd == b"rev":
        motor.dc(-50)
    else:
        motor.stop()"""

import os
path = input("name:")
hi = os.path.dirname(os.path.abspath(__file__))
hi = os.path.join("'" + hi + "\\" + path + ".py" + "'")
os.system("pybricksdev run --no-stay-connected ble" + hi)
