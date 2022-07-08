import pyautogui
import webbrowser as wb
import time

#Mouse Functions
# Prints the size of the screen
print(pyautogui.size()) #Size(width=1920, height=1080)
# Gives the position of the array
print(pyautogui.position())
# Moves the mouse to the given position
# pyautogui.moveTo(500, 500, 3) #First argument is x-coordinate, second is y-coordinate, third is the time in which it will execute
#Moves the mouse relative to its current position
# pyautogui.moveRel(100, 100, 3) # Arguments are similar as .moveTO()
#Click
# pyautogui.click(960, 500, 3, 3, button="left") #Arguments = (x-coord, y-coord, no.of clicks, duration, which button to click)
# pyautogui.tripleClick()
# pyautogui.doubleClick()
# pyautogui.leftClick()
# pyautogui.rightClick()

#Scrolls up 500
# pyautogui.scroll(500)
#Scrolls down 500
# pyautogui.scroll(-500)

#Moves mouse up and down
# pyautogui.mouseUp(100, 100, button="left")
# pyautogui.mouseDown(100, 100, button="left")
# time.sleep(3)
#Examples of mouse up and down
# pyautogui.mouseDown(300, 400, button="left")
# pyautogui.moveTo(800,400, 3)
# time.sleep(3)
# pyautogui.mouseUp()
# pyautogui.moveTo(1000, 400, 3)

#Keyboard Functions
# pyautogui.write("Hello")
# pyautogui.press("enter")
# pyautogui.press("space")











# To spam whatsapp
# wb.open("web.whatsapp.com")
# time.sleep(20)
# while True:
#     pyautogui.press("K")
#     pyautogui.press("A")
#     pyautogui.press("P")
#     pyautogui.press("I")
#     pyautogui.press("L")
#     pyautogui.press("enter")