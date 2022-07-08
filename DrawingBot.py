# Simple Squaring drawing bot.

import pyautogui as pg
import time

time.sleep(3)

pg.mouseDown(300, 400, button="left")
pg.moveTo(300, 900, 3)
pg.moveTo(800, 900, 3)
pg.moveTo(800, 400, 3)
pg.moveTo(300, 400, 3)
pg.mouseUp()