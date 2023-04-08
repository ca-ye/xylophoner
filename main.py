# Imports
import PySimpleGUI as sg
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo

factory = PiGPIOFactory(host='fe80::584a:22e2:4eff:931f%4')  # Connects to the pi, host is the ip

servo_1 = Servo(21, pin_factory=factory)  # left strike
servo_2 = Servo(20, pin_factory=factory)  # right angle
servo_3 = Servo(26, pin_factory=factory)  # right strike
servo_4 = Servo(19, pin_factory=factory)  # left angle

servo_1.value = 0
servo_2.value = 0
servo_3.value = 0
servo_4.value = 0

keys = {
    "C": 1,
    "D": 2,
    "E": 3,
    "F": 4,
    "G": 5,
    "A": 6,
    "B": 7,
    "C\'": 8
}

def turn_on_servos(event):
    if event == '1':
        servo_4.value = 0.3
        sleep(0.5)
        servo_1.value = 0.7
        sleep(0.5)
        servo_1.value = 0
        sleep(0.5)

    elif event == '2':
        servo_4.value = 0.1
        sleep(0.5)
        servo_1.value = 0.7
        sleep(0.5)
        servo_1.value = 0
        sleep(0.5)

    elif event == '3':
        servo_4.value = -0.05
        sleep(0.5)
        servo_1.value = 0.7
        sleep(0.5)
        servo_1.value = 0
        sleep(0.5)

    elif event == '4':
        servo_4.value = -0.25
        sleep(0.5)
        servo_1.value = 0.7
        sleep(0.5)
        servo_1.value = 0
        sleep(0.5)

    elif event == '5':
        servo_2.value = 0.1
        sleep(0.5)
        servo_3.value = 0.7
        sleep(0.5)
        servo_3.value = 0
        sleep(0.5)

    elif event == '6':
        servo_2.value = -0.1
        sleep(0.5)
        servo_3.value = 0.7
        sleep(0.5)
        servo_3.value = 0
        sleep(0.5)

    elif event == '7':
        servo_2.value = -0.25
        sleep(0.7)
        servo_3.value = 0.7
        sleep(0.5)
        servo_3.value = 0
        sleep(0.5)

    elif event == '8':
        servo_2.value = -0.4
        sleep(0.7)
        servo_3.value = 0.7
        sleep(0.5)
        servo_3.value = 0
        sleep(0.5)

    elif event == 'submit':
        sequence = values['sequence']
        sequence = sequence.split(" ")
        for i in sequence:
            turn_on_servos(str(keys[i]))



sg.theme('DarkBlue6')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Click on the letters to go to that letter on the xylophone.')],
          [sg.Text('Enter a sequence'), sg.InputText(key='sequence')],
          [sg.Button('C', key='1'), sg.Button('D', key='2'), sg.Button('E', key='3'), sg.Button('F', key='4'),
           sg.Button('G', key='5'), sg.Button('A', key='6'),
           sg.Button('B', key='7'), sg.Button('C\'', key='8'), sg.Button('Enter Sequence', key='submit')]]

window = sg.Window('XYLOPHONER', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        servo_1.value = 0
        servo_2.value = 0
        servo_3.value = 0
        servo_4.value = 0
        break
    turn_on_servos(event)

window.close()
