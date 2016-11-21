import machine
import time

import nunchuck

nun = nunchuck.Nunchuck(machine.I2C(
        scl=machine.Pin(5),
        sda=machine.Pin(4),
        freq=100000
        ))

x = 0
y = 0
while True:
    if not nun.joystick_center():
        if nun.joystick_up():
            y += 1
        elif nun.joystick_down():
            y -= 1
        if nun.joystick_left():
            x -= 1
        elif nun.joystick_right():
            x += 1
    print(x, y, nun.joystick_x(), nun.joystick_y())

    j = nun.joystick()
    a = nun.accelerator()
    b = nun.buttons()
    print("Joystick: X={0: <3} Y={1: <3} Accelerator: X={2: <3} Y={3: <3} Z={4: <3} Buttons: C={5} Z={6}".format(
            j[0], j[1],
            a[0], a[1], a[2],
            b[0], b[1]
            ))

    time.sleep_ms(100)
