import pyfirmata
from tkinter import *
from pynput import keyboard

board = pyfirmata.Arduino('/dev/ttyUSB0')

iter8 = pyfirmata.util.Iterator(board)
iter8.start()

pin11 = board.get_pin('d:11:s')
pin10 = board.get_pin('d:10:s')
pin6 = board.get_pin('d:6:s')
pin5 = board.get_pin('d:5:s')

servo1_pos = 90
servo2_pos = 80
servo3_pos = 85
servo4_pos = 100

pin11.write(servo1_pos)
def move_servo_1(a):
    global servo1_pos
    servo1_pos = a
    pin11.write(a)

pin10.write(servo2_pos)
def move_servo_2(b):
    global servo2_pos
    servo2_pos = b
    pin10.write(b)

pin6.write(servo3_pos)
def move_servo_3(c):
    global servo3_pos
    servo3_pos = c
    pin6.write(c)

pin5.write(servo4_pos)
def move_servo_4(d):
    global servo4_pos
    servo4_pos = d
    pin5.write(d)

def on_press(key):
    global servo1_pos, servo2_pos, servo3_pos, servo4_pos
    try:
        ## Verde
        ## Definir posição inicial do servo 1 (pin11)
        if key.char == 'd':
            servo1_pos = max(0, servo1_pos - 5)
            move_servo_1(servo1_pos)
        elif key.char == 'a':
            servo1_pos = min(180, servo1_pos + 5)
            move_servo_1(servo1_pos)

        ## Amarelo
        ## Definir posição inicial do servo 2 (pin10)
        elif key.char == 'w': # AVANÇAR
            servo2_pos = min(180, servo2_pos + 5)
            move_servo_2(servo2_pos)
        elif key.char == 's': # RECUAR
            servo2_pos = max(0, servo2_pos - 5)
            move_servo_2(servo2_pos)

        ## Laranja
        ## Definir posição inicial do servo 3 (pin6)
        elif key.char == 'i': # SUBIR
            servo3_pos = min(180, servo3_pos + 5)
            move_servo_3(servo3_pos)
        elif key.char == 'k': # DESCER
            servo3_pos = max(0, servo3_pos - 5)
            move_servo_3(servo3_pos)

        ## Azul
        ## Definir posição inicial do servo 4 (pin5)
        elif key.char == 'o': # ABRI
            servo4_pos = min(100, servo4_pos + 5)
            move_servo_4(servo4_pos)
        elif key.char == 'p': # FECHA
            servo4_pos = max(180, servo4_pos - 5)
            move_servo_4(servo4_pos)

    except AttributeError:
        pass

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:

    listener.join()


