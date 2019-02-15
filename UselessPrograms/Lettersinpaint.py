import pyautogui
import random

pyautogui.hotkey('altleft', 'tab')

# colors = [[886,75],[915,75],[940,75],[970,75],[999,75],[1026,75],[1051,75],[1083,75]]
colors = [[886,102],[915,102],[940,102],[970,102],[999,102],[1026,102],[1051,102],[1083,102]]
# colors = [[886,130],[915,130],[940,130],[970,130],[999,130],[1026,130],[1051,130],[1083,130]]

artMinX = 5+10
artMinY = 178+10
artMaxX = 1891-10
artMaxy = 982-10

def draw(letter):
	if letter == "n":
		pyautogui.dragRel(0, 10, 0)
		pyautogui.moveRel(0, -10, 0)
		pyautogui.dragRel(13, 7.5, 0)
		pyautogui.dragRel(0, -10, 0)
	if letter == "k":
		pyautogui.dragRel(0, 10, 0)
		pyautogui.moveRel(0, -5, 0)
		pyautogui.dragRel(9, -5, 0)
		pyautogui.moveRel(-9, 5, 0)
		pyautogui.dragRel(9, 5, 0)


# N in paint
for y in range(artMinY,artMaxy,200):
	for x in range(artMinX,artMaxX,200):
		ran = random.randint(0,7)
		pyautogui.click(colors[ran][0],colors[ran][1],2,0.2,button='left')
		pyautogui.click(x,y)
		draw("k")
