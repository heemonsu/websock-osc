import websocket
import thread
import time

import rospy
import std_msgs


def on_message(ws, message):
	words = message[1:-1].split(",")
	skeleton = []
	pub = rospy.Publisher('pyclient/skeleton_data', std_msgs.MultiArray, quee_size=1)
	if words[0] == "Right_Shoulder" or "Right_Hand" or "Left Shoulder" or "Left Wrist":
		words_timestamped = words.append(0)
		skeleton.append(words_timestamped)
	if len(skeleton) == 4:
		# Write the correct publish data
		pub.publish(words_timestamped)
		rospy.loginfo(words_timestamped)

def on_error(ws, error):
	print(error)

def on_close(ws):
	print("Closed connection!")

def on_open(ws):
	ws.readyState = 1
	print("opened connection")


if __name__ == '__main__':
	try:
		rospy.init_node('kinect_data', anonymous=True)
		websocket.enableTruce(True)
		ws = websocket.WebSocketApp("ws://130.215.206.245:3000", on_message=on_message, on_error=on_error, on_close=on_close)
		ws.on_open = on_open
		ws.run_forever()
	except KeyboardInterrupt:
		ws.close()
