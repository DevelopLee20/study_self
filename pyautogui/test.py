from selenium import webdriver

# 기본 설정
url = 'https://www.naver.com/'
id = '아이디'
pw = '비밀번호'
#

mobile_emulation = {"deviceName": "iPhone X"}
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome("C:/Users/cslab/Desktop/vscoding/study_self/pyautogui/chromedriver.exe", options=chrome_options)

driver.get(url)