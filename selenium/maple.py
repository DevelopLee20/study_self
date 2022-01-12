from selenium import webdriver

id = 'solsan24@hanmail.com'
pw = 'hansan24!!'

driver = webdriver.Chrome('C:\Users\dldls\바탕 화면\Coding\study_self\selenium\chromedriver.exe')

driver.get('https://maplestory.nexon.com/Home/Main')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="section02"]/div/div[2]/span[2]/a/img').click()
driver.find_element_by_id('mid').send_keys(id)
driver.find_element_by_id('mpw').send_keys(pw)