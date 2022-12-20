import pyautogui, time, random


print(pyautogui.size())

while True:
    
	x = random.randrange(0,1440,1)
	y = random.randrange(0, 900, 1)	
	pyautogui.moveTo(x,y,duration = 5)
	print(time.ctime(time.time()))
