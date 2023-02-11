# Imports
import PySimpleGUI as sg
from gpiozero import LED, Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo

factory = PiGPIOFactory(host='192.168.0.26')  # Connects to the pi, host is the ip
led_1 = LED(21, pin_factory=factory)  # First number is the GPIO number
led_2 = LED(20, pin_factory=factory)
led_3 = LED(26, pin_factory=factory)
led_4 = LED(16, pin_factory=factory)
led_5 = LED(19, pin_factory=factory)
led_6 = LED(13, pin_factory=factory)
led_7 = LED(12, pin_factory=factory)
led_8 = LED(6, pin_factory=factory)
servo = Servo(17, pin_factory=factory)


# buttons = {           used for testing
#     "1": led_1,
#     "2": led_2,
#     "3": led_3,
#     "4": led_4,
#     "5": led_5,
#     "6": led_6,
#     "7": led_7,
#     "8": led_8
# }

# def turn_on_leds(event):
#     buttons[event].on()
#     sleep(1)
#     buttons[event].off()

def servoTest():  # Test code, requires the dictionary method as shown in the led test for controlling multiple servos
    servo.value = 0.666666666  # Value of servo is defined as a decimal of the servo's turning circle
    sleep(3)
    servo.value = 0.111111111  # 1 is max, -1 is min
    sleep(3)
    servo.value = -0.111111111
    sleep(3)
    servo.value = -0.666666666
    sleep(3)
    servo.value = 0


sg.theme('DarkBlue6')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Click on the letters to go to that letter on the xylophone.')],
          [sg.Text('Enter a sequence'), sg.InputText()],
          [sg.Button('C', key='1'), sg.Button('D', key='2'), sg.Button('E', key='3'), sg.Button('F', key='4'),
           sg.Button('G', key='5'), sg.Button('A', key='6'),
           sg.Button('B', key='7'), sg.Button('C', key='8'), sg.Button('Rest')]]

window = sg.Window('XYLOPHONER', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    print('You entered', event)
    servoTest()
    # turn_on_leds(event)

window.close()
