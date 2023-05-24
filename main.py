import datetime
from datetime import timedelta, date

import time
import config
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    # chorme driver
    driver = webdriver.Chrome('./chromedriver')
    # 서울 공공서비스 예약
    reservation_url = config.reservation_url
    # 에코파크 풋살장
    futsal_place1 = config.futsal_place1
    # 마루공원 풋살장 1면
    futsal_place2 = config.futsal_place2
    # 마루공원 풋살장 2면
    futsal_place3 = config.futsal_place3

    # 사용자 정보
    name = config.name
    phone_number = config.phone_number
    id = config.id
    password = config.password

    # 예약 정보
    reservation_date = datetime.datetime(2023, 6, 7)
    tomorrow = date.today() + timedelta(1)
    before_date = reservation_date - timedelta(1)

    # unit10 = 8~9
    # unit11 = 9~10
    times = ['unit3', 'unit4']

    # 예약할 구장
    futsal_place = futsal_place1

    # 예약페이지 Open
    url = f'{reservation_url}?rsv_svc_id={futsal_place}'
    driver.get(url)

    # time.sleep(1)

    # 팝업 제거
    searchPath = '//span[text()="팝업닫기"]/..'
    btn_pop_close = driver.find_element(By.XPATH, searchPath)
    btn_pop_close.click()
    # time.sleep(1)

    # 로그인 페이지 오픈
    loginPath = '//*[@id="header"]/div[1]/div/div[1]/a'
    login_button = driver.find_element(By.XPATH, loginPath).click()

    # login = driver.find_element(By.XPATH, '//a[text()="로그인"]')
    # login.click()

    user_id = driver.find_element(By.ID, 'userid')
    user_id.send_keys(id)
    user_pwd = driver.find_element(By.ID, 'userpwd')
    user_pwd.send_keys(password)
    time.sleep(1)
    login = driver.find_element(By.CLASS_NAME, 'btn_login')
    login.click()
    time.sleep(1)

    # 팝업 제거
    searchPath = '//span[text()="팝업닫기"]/..'
    btn_pop_close = driver.find_element(By.XPATH, searchPath)
    btn_pop_close.click()

    # 내일 날짜 클릭
    driver.find_element(By.ID, f'cal_{tomorrow.strftime("%Y%m%d")}').click()

    # 예약버튼 클릭
    searchPath = '//a[text()="예약하기"]'
    driver.find_element(By.XPATH, searchPath).click()

    # # 전날 예약 page로 이동
    # url = f'{reservation_url}?rsv_svc_id={futsal_place}'
    # driver.get(login_url)

    # 다음 달
    driver.find_element(By.CLASS_NAME, 'cal_next').click()

    # 인증번호 발송
    # searchPath = '//button[contains(@onclick,"fnCertifi")]'
    # driver.find_element(By.XPATH, searchPath).click()
    # time.sleep(30)

    while True:
        time.sleep(1)
        try:
            date_block = driver.find_element(By.ID, f'cal_{reservation_date.strftime("%Y%m%d")}')
        except:
            driver.find_element(By.CLASS_NAME, 'cal_next').click()

        date_block = driver.find_element(By.ID, f'cal_{reservation_date.strftime("%Y%m%d")}')
        if date_block.get_attribute('title') != '예약가능':
            driver.find_element(By.CLASS_NAME, 'cal_next').click()
            driver.find_element(By.CLASS_NAME, 'cal_prev').click()
            continue

        # 예약버튼 클릭
        # searchPath = '//a[text()="예약하기"]'
        # reservation_button = driver.find_element(By.XPATH, searchPath).click()

        time.sleep(1)

        date_block = driver.find_element(By.ID, f'cal_{reservation_date.strftime("%Y%m%d")}').click()
        time.sleep(0.2)

        time1 = driver.find_element(By.ID, f'{times[0]}').find_element(By.TAG_NAME, 'a').click()
        time.sleep(0.2)

        time2 = driver.find_element(By.ID, f'{times[1]}').find_element(By.TAG_NAME, 'a').click()
        time.sleep(0.2)

        driver.find_element(By.ID, 'addItem1').send_keys('동의합니다.')

        # 이름
        driver.find_element(By.ID, f'form_name2').send_keys(name)

        # 휴대전화 번호
        driver.find_element(By.ID, f'moblphone2').send_keys(phone_number)

        searchPath = '//*[@id="chk_agree_all"]'
        check_box = driver.find_element(By.XPATH, searchPath)

        driver.execute_script("arguments[0].checked = true;", check_box)
        # 모두 동의 체크
        # chk_agree_all = driver.find_element(By.ID, 'chk_agree_all')
        # chk_agree_all.click()



        break