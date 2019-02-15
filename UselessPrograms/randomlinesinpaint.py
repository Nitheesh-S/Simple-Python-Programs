import pyautogui
import random

pyautogui.hotkey('altleft', 'tab')

colors = [[886,75],[915,75],[940,75],[970,75],[999,75],[1026,75],[1051,75],[1083,75]]

# for x in range(10):
# 	x1 = random.randint(100, 1800)
# 	y1 = random.randint(200, 882)
# 	x2 = random.randint(100, 1800)
# 	y2 = random.randint(200, 882)
# 	pyautogui.moveTo(x1,y1)
# 	pyautogui.dragTo(x2,y2)
# 	ran = random.randint(0,7)
# 	pyautogui.click(colors[ran][0],colors[ran][1],2,0.2,button='left')


count = 0
while (count < 10):
	count = count+1
	x1 = random.randint(100, 1800)
	y1 = random.randint(200, 882)
	x2 = random.randint(100, 1800)
	y2 = random.randint(200, 882)
	pyautogui.moveTo(x1,y1)
	pyautogui.dragTo(x2,y2)
	ran = random.randint(0,7)
	pyautogui.click(colors[ran][0],colors[ran][1],2,0.2,button='left')    
	print(count)

# N in paint
# for y in range(200,882,200):
	# for x in range(100,1800,200):
# 		pyautogui.click(x,y)
# 		pyautogui.dragRel(0, 10, 0)
# 		pyautogui.moveRel(0, -10, 0)
# 		pyautogui.dragRel(13, 7.5, 0)
# 		pyautogui.dragRel(0, -10, 0)


# random lines in paint
# for x in range(100):
# 	x1 = random.randint(100, 1800)
# 	y1 = random.randint(200, 882)
# 	x2 = random.randint(100, 1800)
# 	y2 = random.randint(200, 882)
# 	pyautogui.moveTo(x1,y1)
# 	pyautogui.dragTo(x2,y2)



# artMinX = 5 
# artMinY = 178
# artMaxX = 1891
# artMaxy = 982

# pyautogui.moveTo(xMax,yMax)