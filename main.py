# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.                                                                                                    123
import os
import time
import pyautogui as pag
import pyautogui

width = 0
height = 0

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # try:
    #     while True:
    #         print("Press Ctrl-C to end")
    #         screenWidth, screenHeight = pag.size()  # 获取屏幕的尺寸
    #         print(screenWidth, screenHeight)
    #         x, y = pag.position()  # 获取当前鼠标的位置
    #         posStr = "Position:" + str(x).rjust(4) + ',' + str(y).rjust(4)
    #         print(posStr)
    #         time.sleep(0.2)
    #         pyautogui.rightClick()
    #         os.system('cls')  # 清楚屏幕
    # except KeyboardInterrupt:
    #     print('end....')
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tuple = pyautogui.size()
    print("width = "+str(tuple[0])+",height = "+str(tuple[1]))
    width = tuple[0]
    height = tuple[1]
    #点击战斗
    pyautogui.moveTo(width/2, height*0.8)
    time.sleep(0.5)
    # 点击上阵战斗
    pyautogui.moveTo(width*0.9, height*0.8)
    time.sleep(5)
    # 点击胜利
    pyautogui.moveTo(width/2, height*0.7)
    time.sleep(1)
    # 点击下一关卡
    pyautogui.moveTo(width / 2, height * 0.8)
    time.sleep(5)
    # 点击搜寻
    pyautogui.moveTo(width / 2, height * 0.7)
    time.sleep(2)

    # pyautogui.dragRel(0, -300)
    # pyautogui.doubleClick()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




















#1234656