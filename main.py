import time
import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    # chorme driver
    driver = webdriver.Chrome('./chromedriver')
    # 서울 공공서비스 예약
    soeul_url = config.soeul_url
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

    # 예약일
    reservation_date = '20221214'
    reservation_date_test = '20221213'

    # unit10 = 8~9
    # unit11 = 9~10
    times = ['unit14', 'unit15']
    # times = ['unit2', 'unit3']

    # 풋살장소 선택
    futsal_place = futsal_place2

    # 예약페이지 Open
    url = f'{soeul_url}?rsv_svc_id={futsal_place}&tr_code=yeyak'
    driver.get(url)

    time.sleep(1)

    # 팝업 제거
    searchPath = '//span[text()="팝업닫기"]/..'
    btn_pop_close = driver.find_element(By.XPATH, searchPath)
    # btn_pop_close = driver.find_element_by_xpath(searchPath)
    btn_pop_close.click()
    time.sleep(1)


    login = driver.find_element(By.XPATH, '//a[text()="로그인"]')
    login.click()

    user_id = driver.find_element(By.ID, 'userid')
    user_id.send_keys(id)
    user_pwd = driver.find_element(By.ID, 'userpwd')
    user_pwd.send_keys(password)
    time.sleep(1)
    login = driver.find_element(By.CLASS_NAME, 'btn_login')
    login.click()

    is_first = True

    while True:
        if is_first:
            time.sleep(2)
            # 팝업 제거
            searchPath = '//span[text()="팝업닫기"]/..'
            btn_pop_close = driver.find_element(By.XPATH, searchPath)
            # btn_pop_close = driver.find_element_by_xpath(searchPath)
            btn_pop_close.click()

            try:
                print('이번달')
                date_block = driver.find_element(By.ID, f'cal_{reservation_date_test}')
            except:
                print('다음달')
                next_month = driver.find_element(By.CLASS_NAME, 'cal_next')
                next_month.click()
                time.sleep(1)
            print('예약페이지 접속')
            date_block = driver.find_element(By.ID, f'cal_{reservation_date_test}')

            date_block.click()
            # 예약버튼 클릭
            searchPath = '//a[text()="예약하기"]'
            reservation_button = driver.find_element(By.XPATH, searchPath).click()

            time.sleep(1)
            is_first = False

        print('날짜 확인')
        # 예약 일자 선택
        time.sleep(1)
        date_block = driver.find_element(By.ID, f'cal_{reservation_date}')
        print('예약 가능 확인')
        if date_block.get_attribute('title') != '예약가능':
            print('예약 불가')
            driver.refresh()
            continue

        print('예약 가능')

        date_block = driver.find_element(By.ID, f'cal_{reservation_date}').click()
        time.sleep(0.2)

        time1 = driver.find_element(By.ID, f'{times[0]}').find_element(By.TAG_NAME, 'a').click()
        # time.sleep(0.2)

        time2 = driver.find_element(By.ID, f'{times[1]}').find_element(By.TAG_NAME, 'a').click()
        # time.sleep(0.2)

        driver.find_element(By.ID, 'addItem1').send_keys('동의합니다.')

        # # 신청자 정보와 동일
        # chk_info = driver.find_element(By.ID, 'chk_info').click()

        # 단체
        # driver.find_element(By.ID, 'radio_user_type1').click()

        # 단체명
        # driver.find_element(By.ID, f'grp_nm').send_keys('단비교육')

        # 이름
        driver.find_element(By.ID, f'form_name2').send_keys(name)

        # 휴대전화 번호
        driver.find_element(By.ID, f'moblphone2').send_keys(phone_number)

        # # 모두 동의 체크
        # driver.find_element(By.ID, 'chk_agree_all').send_keys(Keys.ENTER)
        # driver.find_element(By.CLASS_NAME, 'vchkbox').send_keys(Keys.ENTER)
        #
        #
        # # 인증번호 발송
        # print('인증번호발송')
        # driver.find_element(By.CLASS_NAME, 'form_phon').find_element(By.CLASS_NAME, 'btn_inp').send_keys(Keys.ENTER)
        #
        # #
        # # driver.execute_script("document.getElementById('chk_agree_all').style.display='none';")
        # # time.sleep(1)
        # # # 인증번호 발송
        # # searchPath = '//button[contains(@onclick,"fnCertifi")]'
        # # driver.find_element(By.XPATH, searchPath).click()
        # time.sleep(0.5)

        break
