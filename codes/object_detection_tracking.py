import numpy as np
import time
import serial
import jetson.inference
import jetson.utils

ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.4)
camera = jetson.utils.videoSource("/dev/video0")
# display = jetson.utils.videoOutput("display://0")


def make_command(cmd,left_speed,right_speed):
	cmd_to_arduino = cmd + chr(int(left_speed)) + chr(int(right_speed))
	return cmd_to_arduino

def nothing(x):
	pass

# cam = cv2.VideoCapture(0)
move = False
cmd = 'S'
left_speed = 0
right_speed = 0
zero_str = 'S' + chr(0) + chr(0)

try:
	#while display.IsStreaming():
	while True:
		img = camera.Capture()
		detections = net.Detect(img)
		print(detections)
		print(type(detections))
		print('\n\n')
		# display.Render(img)
		# display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))


		# (x,y,w,h)=cv2.boundingRect(cnt)
		# 	if area >= 300:
		# 		x_cord = x + w/2
		# 		move = True
		# 		print("Object detected at " + str(x_cord))

		# 	else:
		# 		x_cord = 720/2
		# 		move = False


		# if(move):
		# 	if(x_cord < 320):       #let there be 40px deadband each side of center of screen
		# 		left_speed = (x_cord/360)*62 + 64
		# 		right_speed = 126

		# 	elif(x_cord > 400):
		# 		left_speed = 126
		# 		right_speed = ((720 - x_cord)/360)*62 + 64

		# 	else:
		# 		left_speed = 126
		# 		right_speed = 126

		# else:
		# 	left_speed = 95
		# 	right_speed = 95

		# command = make_command(cmd, left_speed, right_speed)
		# ser.write(command.encode())


		#time.sleep(0.1)
		#end = time.time()

		#print(end-start)
		#time.sleep(0.25)

except KeyboardInterrupt:
	ser.write(zero_str.encode())
