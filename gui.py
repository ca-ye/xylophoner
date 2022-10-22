# sockets reference: https://stackoverflow.com/questions/19104242/how-to-send-a-message-from-the-server-to-a-client-using-sockets
from venv import create
import PySimpleGUI as sg
import socket

HOST = '192.168.0.152'
PORT = 65439

ACK_TEXT = 'text_received'

def sendToSocket(message, sock):
	# encode the text message
	encodedMessage = bytes(message, 'utf-8')

	# send the data via the socket to the server
	sock.sendall(encodedMessage)

	# receive acknowledgment from the server
	encodedAckText = sock.recv(1024)
	ackText = encodedAckText.decode('utf-8')

	# log if acknowledgment was successful
	if ackText == ACK_TEXT:
		print('server acknowledged reception of text')
	else:
		print('error: server has sent back ' + ackText)

def createGUI(sock):
	sg.theme('DarkBlue6')   # Add a touch of color
	# All the stuff inside your window.
	layout = [  [sg.Text('Click on the letters to go to that letter on the xylophone.')],
				[sg.Text('Enter a sequence'), sg.InputText(key = "text_input", do_not_clear=False), sg.Button('Send')],
				[sg.Button('C'), sg.Button('D'), sg.Button('E'), sg.Button('F'), sg.Button('G'), sg.Button('A'), sg.Button('B'), sg.Button('G'), sg.Button('Rest') ]]

	# Create the Window
	window = sg.Window('XYLOPHONER', layout)
	# Event Loop to process "events" and get the "values" of the inputs
	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
			break
		elif event == "Send":
			notes = values["text_input"]
			sendToSocket(notes, sock)
		elif (event == "C" 
			or event == "D"
			or event == "E"
			or event == "F"
			or event == "G"
			or event == "A"
			or event == "B"
			or event == "G"
			or event == "Rest"):
				sendToSocket(event, sock)

	window.close()

if __name__ == "__main__":
	# instantiate a socket object
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print('socket instantiated')

	# bind the socket
	sock.bind((HOST, PORT))
	print('socket binded')

	# start the socket listening
	sock.listen()
	print('socket now listening')

	# accept the socket response from the client, and get the connection object
	conn, addr = sock.accept()      # Note: execution waits here until the client calls sock.connect()
	print('socket accepted, got connection object')
	
	createGUI(sock)
