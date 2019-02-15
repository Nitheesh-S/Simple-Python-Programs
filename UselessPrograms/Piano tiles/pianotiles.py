# http://tanksw.com/piano-tiles/
# http://www.bestgames.com/Piano-Tiles-2

# def get_pixel_colour(i_x, i_y):
#     import PIL.ImageGrab
#     return PIL.ImageGrab.grab().load()[i_x, i_y]

def get_pixel_colour(i_x, i_y):
    import win32gui
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    return (i_colour & 0xff)
    # return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

# r, g, b = get_pixel_colour(500, 500)

# print(r)

import pyautogui as pg
import time

pg.hotkey('altleft', 'tab')

# pg.click(x,y)
# start = time.time();
# top1 = [817,179]
# point1 = [779,640]
# point2 = [919,640]
# point3 = [961,640]
# point4 = [1086,640]
# points = [[779,640],[919,640],[961,640],[1086,640]]
# points = [779,919,961,1086]

    # for y in range(179,640,1):
    # while (179,640,1):
# row = 640
# count = score = comp = 0

while True:
    for col in [779,919,961,1086]:
        if get_pixel_colour(col,640) < 20:
            pg.click(col,650)
            continue

# count += 1
# score += count
# count = 0
# comp = round(score/3) + 400
# print(row,comp)
# if row > 300 and count == 0:
#     row -= 1

# print(score)
# end = time.time();
# print(start,end)

# while True:
#     r1= get_pixel_colour(point1[0], 640)
#     if r1 == 0:
#         pg.click(point1[0],640)
#         continue
#     r2= get_pixel_colour(point2[0], 640)
#     if r2 == 0:
#         pg.click(point2[0],640)
#         continue
#     r3= get_pixel_colour(point3[0], 640)
#     if r3 == 0:
#         pg.click(point3[0],640)
#         continue
#     r4= get_pixel_colour(point4[0], 640)
#     if r4 == 0:
#         pg.click(point4[0],640)
#         continue
#     if r1 == 83:
#         break
    # time.sleep(0.1)
print("done")


# col1=817, y=613
# col2=935, y=614
# col3=957, y=614
# col4=1079, y=614


# numpy as np
# from pil import imagegrab
# import cv2
# from  directKeys import click