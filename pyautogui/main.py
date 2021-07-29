import time

import pyautogui as auto

def Loop():
    # auto.press('f5')
    # auto.scroll(-600)
    auto.click('choice.PNG')

Loop()

while 0:
    tm = time.ctime()
    time_check = str(tm[11:19])
    if time_check == '00:00:00':
        # 매크로 내용 작성
        pass
    print("time:", time_check)