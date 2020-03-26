import pyautogui
import time

with open('data.txt', "r") as f:
	commands = [line.rstrip() for line in f]

commands_counter = 0

# perform actions
while True:
	try:
		cmd = commands[commands_counter]
		cmd_split = cmd.split()
		try:
			cmd_int_list = [int(i) for i in cmd_split[1:]]
		except ValueError:
			cmd_int_list = []

		if cmd_split[0] == 'click':
			if len(cmd_int_list) == 0:
				pyautogui.click()
			elif len(cmd_int_list) <= 2:
				pyautogui.click(x = cmd_int_list[0],y = cmd_int_list[1])
		elif cmd_split[0] == 'scroll':
			if len(cmd_int_list) <= 1:
				pyautogui.hscroll(cmd_int_list[0])
		elif cmd_split[0] == 'enter':
			pyautogui.press('enter')
		elif cmd_split[0] == 'sleep':
			time.sleep(1)
		elif cmd_split[0] == 'sleep_0.5':
			time.sleep(0.5)
		elif cmd_split[0] == 'paste':
			pyautogui.hotkey('ctrl', 'v')

		time.sleep(1)
		if commands_counter >= len(commands)-1:
			commands_counter = 0
		else:
			commands_counter+=1
	except KeyboardInterrupt:
		break
	except EOFError:
		break