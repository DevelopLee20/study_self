from selenium import webdriver

# Mobile View settings
mobile_emulation = {"deviceName": "iPhone X"}
chrome_options = webdriver.ChromeOptions()

# image Block
# 이미지 블락 처리하면 로딩향상되나 보안패드 숫자도 사라집니다.
# 다른 변수 이용해서 사용가능하신분은 사용하시면 좋아요.
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Mobile View add option
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# 크롬드라이버 다운로드 주소입니다.
driver = webdriver.Chrome(
    "chromedriver.exe", chrome_options=chrome_options)
# 로그인 페이지 로딩
driver.get('https://www.naver.com/')