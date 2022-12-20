import pyautogui, time, random

print(pyautogui.size())  
# output: screen resolution in the format(x,y)
while True:
    
	x = random.randrange(0,1440,1) # 1440 -> value of x
	y = random.randrange(0, 900, 1)	# 990 -> value of y
	pyautogui.moveTo(x,y,duration = 5) # moves cursor to randomized points generated every 5 seconds
	print(time.ctime(time.time())) # displays string notion of currentTime
 
 
