from email import *
from time import *
from gpio import *

def onEmailReceive(sender, subject, body):
	print("Received from: " + sender)
	print("Subject: " + subject)
	print("Body: " + body)

def onEmailSend(status):
	print("send status: " + str(status))

def main():
	EmailClient.setup(
		"room1@hospital.com",
		"hospital.com",
		"room1",
		"room1"
	)
	room_counter = 0;
	EmailClient.onReceive(onEmailReceive)
	EmailClient.onSend(onEmailSend)
	while True:
		cardReader_o = digitalRead(0);
		cardReader_i = digitalRead(1);

		if (cardReader_o != 0 and room_counter == 0):
			function_counter = 0;
			EmailClient.send("room_management@hospital.com", "Room1 Notification", "Patient Enter")
			room_counter += 1
			print(room_counter)
			sleep(1)
		elif (cardReader_i != 0 and room_counter != 0):
			EmailClient.send("room_management@hospital.com", "Room1 Notification", "Patient Exit")
			room_counter -= 1
			print(room_counter)
			sleep(1)
		else:
			sleep(1)
			print(cardReader_o,cardReader_i)
	sleep(1)
	# check email once a while
	while True:
		EmailClient.receive()
		sleep(5)

if __name__ == "__main__":
	main()
