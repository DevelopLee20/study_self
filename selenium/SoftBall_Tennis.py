from selenium import webdriver

# 아이디, 비번, 코트번호, 시작시간, 대여시간, 인원, 행사명, 라이트설정:개수
def WebMaster(user_id, user_pw, court, hour, unit, many, title, light):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    driver.get('https://re.asimc.or.kr/v')

    # 로그인
    try:
        driver.implicitly_wait(0.5)
        driver.find_element_by_xpath('//*[@id="topLogin"]').click()
        driver.find_element_by_id('userId').send_keys(user_id)
        driver.find_element_by_id('password').send_keys(user_pw)
        driver.find_element_by_xpath('//*[@id="login_wrap"]/table/tbody/tr[5]/td/div/a').click()
    except:
        print("로그인 실패\n")
        return

    # 시설 예약 바로가기 설정 후 진입
    try:
        # 7: 국제정구장
        # 32: 1코트, 90~96: 2~8코트
        driver.implicitly_wait(0.5)
        webdriver.support.ui.Select(driver.find_element_by_id('fac_list')).select_by_value('7')
        court_list = [32,90,91,92,93,94,95,96]
        webdriver.support.ui.Select(driver.find_element_by_id('det_fac_list')).select_by_value(f'{court_list[court-1]}')
        driver.find_element_by_xpath('//*[@id="main_res_t"]/tbody/tr/td[3]/a').click()
    except:
        print("시설 예약 진입 실패")
        return

    # 진입 후 날짜 선택
    try:
        # 체육경기 = A, 경기이외의 행사 = O
        driver.implicitly_wait(0.5)
        ##### 바로 아래에 날짜 선택하는 옵션 추가
        driver.find_element_by_xpath('//*[@id="cal_body"]/tr[3]/td[4]').click()
        webdriver.support.ui.Select(driver.find_element_by_id('purpose')).select_by_value('A')
        if hour < 10:
            webdriver.support.ui.Select(driver.find_element_by_id('s_time_hour')).select_by_value(f'0{hour}')
        else:
            webdriver.support.ui.Select(driver.find_element_by_id('s_time_hour')).select_by_value(f'{hour}')
        webdriver.support.ui.Select(driver.find_element_by_id('hour_unit')).select_by_value(f'{unit}')
        driver.find_element_by_xpath('//*[@id="more"]/a').click()
    except:
        print("날짜 선택 오류")
        return

    # 인원수, 행사명 작성
    try:
        driver.implicitly_wait(0.5)
        driver.find_element_by_id('person').send_keys(f'{many}')
        driver.find_element_by_id('event').send_keys(f'{title}')
        driver.find_element_by_xpath('//*[@id="join_btn_wrap"]/a[1]').click()
    except:
        print("정보 입력 오류")
        return

    # 라이트 설정
    try:
        # 라이트 설정 라이트_value = 23
        driver.implicitly_wait(0.5)
        driver.find_element_by_xpath('//*[@id="sub_fac_cnt"]').clear()
        driver.implicitly_wait(0.3)
        driver.find_element_by_id('sub_fac_cnt').send_keys(light)

        if light:
            driver.find_element_by_xpath('//*[@id="join_table"]/table/tbody/tr[1]/td[2]/form/a').click()
    except:
        print("라이트 설정 오류")
        return

    # 최후의 통첩 : 테스트할땐 주석 후 테스트, 실제만 사용
    # driver.find_element_by_xpath('//*[@id="join_btn_wrap"]/a[1]').click()

# 아이디, 비번, 코트번호, 시작시간, 대여시간, 인원, 행사명, 라이트설정:개수