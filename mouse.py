import pyautogui
import time
# get position mouse

while True:
	try:
		x,y = pyautogui.position()
		print(x,y)
		time.sleep(0.5)
	except KeyboardInterrupt:
		break
	except EOFError:
		break
