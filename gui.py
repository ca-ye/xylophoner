import PySimpleGUI as sg
import time

sg.theme('DarkBlue6')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Click on the letters to go to that letter on the xylophone.')],
            [sg.Text('Enter a sequence'), sg.InputText()],
            [sg.Button('C'), sg.Button('D'), sg.Button('E'), sg.Button('F'), sg.Button('G'), sg.Button('A'), sg.Button('B'), sg.Button('G'), sg.Button('Rest') ]]

# Create the Window
window = sg.Window('XYLOPHONER', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', event[0])

window.close()