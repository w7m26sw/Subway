from datetime import date
import time
import random
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


PATH = "F:/GitHub/Subway/edgedriver_win64/msedgedriver.exe"
url = "SubwayURL" #subway 問卷 URL


today = time.strftime("%m/%d/%Y", time.localtime()) 

for i in range(5):
    driver = webdriver.Edge(PATH)
    driver.get(url)

    #隨機email
    randemail = random.choice(list(open('account.txt', 'r', encoding="utf-8")))
    #email
    email = driver.find_element_by_name("spl_q_subway_customer_email_txt")
    email.send_keys(f"{randemail}@gmail.com")
    email_check = driver.find_element_by_name("spl_q_subway_confirm_email_address_txt")
    email_check.send_keys(f"{randemail}@gmail.com")

    #隨機名字
    randname = random.choice(list(open('name.txt', 'r', encoding="utf-8")))
    LAST_NAME = randname[1:3]
    FRIST_NAME = randname[0]

    #名字
    last_name = driver.find_element_by_name("spl_q_subway_customer_first_name_txt")
    last_name.send_keys(LAST_NAME)

    #姓氏
    frist_name = driver.find_element_by_name("spl_q_subway_customer_last_name_txt")
    frist_name.send_keys(FRIST_NAME)
    time.sleep(3)
    button = driver.find_element_by_name("forward_main-pager").click()
    #等待載入
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "srClass"))
        )

    #餐廳編號
    stroe_number = driver.find_element_by_id("storeNumberPart1")
    stroe_number.send_keys("32580")

    #購買日期
    buyday = driver.find_element_by_id("cal_q_subway_receipt_transaction_date_date_")
    buyday.send_keys(today)

    #購買時間
    buy_hour = random.randint(10, 19)
    buy_min = random.randint(10, 50)
    driver.find_element_by_xpath("//div[@id='content']/div[8]/fieldset/div/div/div/div/div/div").click()
    time.sleep(1)
    driver.find_element_by_xpath(f"//div[@id='content']/div[8]/fieldset/div/div/div/div/div[2]/ul/li[{buy_hour}]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='content']/div[9]/fieldset/div/div/div/div/div/div").click()
    time.sleep(1)
    driver.find_element_by_xpath(f"//div[@id='content']/div[9]/fieldset/div/div/div/div/div[2]/ul/li[{buy_min}]").click()
    time.sleep(3)

    driver.find_element_by_id("buttonNext").click()
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "questionCaption"))
        )

    driver.find_element_by_id("onf_q_subway_osat_satisfaction_web_scale_5_5").click()
    driver.find_element_by_id("onf_q_subway_taste_quality_of_the_meal_web_scale_5_5").click()
    driver.find_element_by_id("onf_q_subway_speed_of_service_web_scale_5_5").click()
    driver.find_element_by_id("onf_q_subway_experience_with_staff_web_scale_5_5").click()
    driver.find_element_by_id("onf_q_subway_cleanliness_of_restaurant_web_scale_5_5").click()
    driver.find_element_by_id("onf_q_subway_ltr_likely_scale_11_10").click()
    time.sleep(3)
    #driver.find_element_by_xpath("//button[@id='buttonFinish']/i").click()
    driver.close()

sys.exit()