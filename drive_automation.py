import pyautogui
from time import sleep

pyautogui.hotkey("winleft","r")
sleep(0.5)
pyautogui.typewrite("chrome")
pyautogui.press("enter")
sleep(2)
pyautogui.hotkey("winleft","up")                                                    # forMaximizingChrome
sleep(0.5)
pyautogui.click(194,51)
pyautogui.press("backspace")
pyautogui.typewrite("https://drive.google.com/drive/my-drive", interval = 0.01)
pyautogui.press("enter")
sleep(5)
pyautogui.click(58,198)                                                                  # addInDrive
sleep(0.5)
pyautogui.click(79,256)                                                                  # addFile
sleep(0.5)
pyautogui.typewrite(r"C:\Users\lalpr\Desktop\CURRENT_BILL\sujith_readings_new", interval = 0.01)
pyautogui.press("enter")
