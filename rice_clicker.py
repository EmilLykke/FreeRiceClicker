from screeninfo import get_monitors
import pyautogui
from PIL import Image
from pytesseract import *
import win32api
import win32con
import time 
import keyboard

pytesseract.tesseract_cmd = r"F:\Program Files\Tesseract-OCR\tesseract.exe"

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def sanitize(text):
    if(" " in text):
        text = text.replace(" ","")
    text = text.lower()
    text = text.strip()
    return text

for m in get_monitors():
    if(m.is_primary==True):
        monitor = m

width = monitor.width
height = monitor.height

def findNum(y, num):
    numScreen = pyautogui.screenshot(region=(width*0.5-50,height_off+y,90,40))
    numScreen.save(".\\"+num+".png")

    img = Image.open(num+".png")

    new_size = tuple(4*x for x in img.size)
    img = img.resize(new_size, Image.ANTIALIAS)

    output_num = pytesseract.image_to_string(img)
    output_num = sanitize(output_num)
    # print(output_num)
    return int(output_num)


while keyboard.is_pressed('q') == False:
    time.sleep(6)
    width_off = width*0.5-55
    height_off = height*0.23

    num1_off = 110
    num2_off = 210
    num3_off = 315
    num4_off = 415

    r1, g1, b1 = pyautogui.pixel(int(width_off),int(height_off)+num1_off)
    r2, g2, b2 = pyautogui.pixel(int(width_off),int(height_off)+num2_off)
    r3, g3, b3 = pyautogui.pixel(int(width_off),int(height_off)+num3_off)
    r4, g4, b4 = pyautogui.pixel(int(width_off),int(height_off)+num4_off)

    if r1 != 255:
        click(int(width_off),int(height_off)+num1_off)
        time.sleep(6)
    if r2 != 255:
        click(int(width_off),int(height_off)+num2_off)
        time.sleep(6)
    if r3 != 255:
        click(int(width_off),int(height_off)+num3_off)
        time.sleep(6)
    if r4 != 255:
        click(int(width_off),int(height_off)+num4_off)
        time.sleep(6)
    if r1 == 255 and r2 == 255 and r3 == 255 and r4 == 255:
        screenshot = pyautogui.screenshot(region=(width_off, height_off, 100, 50))
        screenshot.save(r"F:\PROJEKTER\Python\rice_clicker\rice_clicker\savedimage.png")

        img = Image.open("savedimage.png")

        new_size = tuple(6*x for x in img.size)
        img = img.resize(new_size, Image.ANTIALIAS)

        output_result = pytesseract.image_to_string(img)
        output_result = sanitize(output_result)
        output_array = output_result.split("x")

        total = int(output_array[0])*int(output_array[1])
        # print(total)
        num1 = findNum(num1_off, "num1")
        num2 = findNum(num2_off, "num2")
        num3 = findNum(num3_off, "num3")
        num4 = findNum(num4_off, "num4")

        if total == num1:
            click(int(width_off),int(height_off)+num1_off)
        if total == num2:
            click(int(width_off),int(height_off)+num2_off)
        if total == num3:
            click(int(width_off),int(height_off)+num3_off)
        if total == num4:
            click(int(width_off),int(height_off)+num4_off)
        
        print(f"This is TOTAL: {total}")
        print(f"This is num1: {num1}")
        print(f"This is num2: {num2}")
        print(f"This is num3: {num3}")
        print(f"This is num4: {num4}")
        print("=======================================================================\n")