# This is just a simple program to like reels automatically

import pyautogui as pg
import time
# Position to like -> Point(x=976, y=554)
# Position to sith reel -> Point(x=1036, y=520)
print(pg.position())
time.sleep(3)

#Range will be the number of reels you want to Like
for i in range(10):
    pg.moveTo(976, 554, 2)
    pg.doubleClick()
    pg.moveTo(1036, 520, 2)
    pg.leftClick()