import pyfirmata
from tkinter import *

board = pyfirmata.Arduino('/dev/ttyUSB0')

iter8 = pyfirmata.util.Iterator(board)
iter8.start()

pin11 = board.get_pin('d:11:s')
pin10 = board.get_pin('d:10:s')
pin9 = board.get_pin('d:6:s')
pin6 = board.get_pin('d:5:s')

"""################################################################
                            Definições
###############################################################"""

# Definir posição inicial do servo 1 (pin11)
pin11.write(90)

def move_servo_1(a):
    pin11.write(a)

# Definir posição inicial do servo 2 (pin10)
pin10.write(80)

def move_servo_2(b):
    pin10.write(b)

# Definir posição inicial do servo 3 (pin9)
pin9.write(85)

def move_servo_3(c):
    pin9.write(c)

# Definir posição inicial do servo 4 (pin6)
pin6.write(100)

def move_servo_4(d):
    pin6.write(d)

"""################################################################
                               GUI
###############################################################"""

# Iniciar a GUI

root = Tk()
root.geometry("900x200")

# Interface Motor 01
# pin11
# Cor Verde
scale = Scale( root,
             from_=180,
             to=0,
             command = move_servo_1,
             width=30,
             orient = HORIZONTAL,
             label = 'WAY')
scale.set(90)  # definir valor inicial do servo 1
scale.place(x=100,y=50)

# Interface Motor 02
# pin10
# Cor Amarelo
scale = Scale( root,
             from_=80,
             to=180,
             command = move_servo_2,
             width=30,
             orient = HORIZONTAL,
             label = 'PITH 1')
scale.set(80)  # definir valor inicial do servo 2
scale.place(x=300,y=50)

# Interface Motor 03
# pin6
# Cor Laranja
scale = Scale( root,
             from_=150,
             to=20,
             command = move_servo_3,
             width=30,
             orient = VERTICAL,
             label = 'PITH 2')
scale.set(85)  # definir valor inicial do servo 3
scale.place(x=500,y=50)

# Interface Motor 04
# pin5
# Cor azul
scale = Scale( root,
             from_=100,
             to=180,
             command = move_servo_4,
             width=30,
             orient = HORIZONTAL,
             label = 'GARRA')
scale.set(100)  # definir valor inicial do servo 4
scale.place(x=700,y=50)

# run Tk event loop
root.mainloop()
