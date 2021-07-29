import pyautogui

screenWidth, screenHeight = pyautogui.size() # 중요 모니터 사이즈 설정

currentMouseX, currentMouseY = pyautogui.position() # 마우스의 x와 y좌표를 얻는다.

pyautogui.moveTo(100,150) # 마우스 위치 이동

pyautogui.click() # 마우스 클릭
pyautogui.click(100,200) # 마우스 클릭 좌표 설정
pyautogui.click('button.png') # 화면에 있는 그림 클릭
pyautogui.scroll(6) # 스크롤 6회하기

pyautogui.move(0,10) # 10 픽셀만큼 현재 위치를 낮춤
pyautogui.doubleClick() # 마우스 더블 클릭
pyautogui.moveTo(500,500,duration=2, tween=pyautogui.easeInOutQuad) # 트위닝/이징 기능을 사용하여 2초 이상 마우스를 움직입니다.

pyautogui.write('Hello world!', interval=0.25)  # 각 키 사이에 1/4초 간격으로 입력
pyautogui.press('esc')     # Esc 키를 누릅니다. 모든 키 이름은 pyautogui.KEY_NAMES에 있습니다.

pyautogui.keyDown('shift') # Shift 키를 누른 상태로 유지합니다.
pyautogui.press(['left', 'left', 'left', 'left']) # 왼쪽 화살표 키를 4번 누릅니다.
pyautogui.keyUp('shift')   # Shift 키에서 손을 뗍니다.
pyautogui.hotkey('ctrl', 'c') # Ctrl-C 단축키 조합을 누릅니다.
pyautogui.alert('This is the message to display.') # 경고 상자를 표시하고 확인을 클릭할 때까지 프로그램을 일시 중지합니다.