# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://subwaylistens.com/?feedless-subwaylistens-a2e0396b990c43b4c36bcdec66228607")
        driver.find_element_by_id("storeNumberPart1").click()
        driver.find_element_by_id("storeNumberPart1").clear()
        driver.find_element_by_id("storeNumberPart1").send_keys("32580")
        driver.find_element_by_id("cal_q_subway_receipt_transaction_date_date_").click()
        driver.find_element_by_id("cal_q_subway_receipt_transaction_date_date_").click()
        driver.find_element_by_id("cal_q_subway_receipt_transaction_date_date_").click()
        driver.find_element_by_xpath("//div[@id='content']/fieldset/div/button/i").click()
        driver.find_element_by_xpath("//div[@id='content']/fieldset/div/table/tr[6]/td[5]/a/div/span").click()
        driver.find_element_by_xpath("//div[@id='content']/div[8]/fieldset/div/div/div/div/div/div").click()
        driver.find_element_by_xpath("//div[@id='content']/div[8]/fieldset/div/div/div/div/div[2]/ul/li[6]").click()
        driver.find_element_by_xpath("//div[@id='content']/div[9]/fieldset/div/div/div/div/div/div").click()
        driver.find_element_by_xpath("//div[@id='content']/div[9]/fieldset/div/div/div/div/div[2]/ul/li[10]").click()
        driver.find_element_by_id("buttonNext").click()
        driver.find_element_by_id("onf_q_subway_osat_satisfaction_web_scale_5_4").click()
        driver.find_element_by_id("onf_q_subway_taste_quality_of_the_meal_web_scale_5_5").click()
        driver.find_element_by_id("onf_q_subway_speed_of_service_web_scale_5_4").click()
        driver.find_element_by_id("onf_q_subway_experience_with_staff_web_scale_5_5").click()
        driver.find_element_by_id("onf_q_subway_cleanliness_of_restaurant_web_scale_5_4").click()
        driver.find_element_by_id("onf_q_subway_ltr_likely_scale_11_7").click()
        driver.find_element_by_xpath("//button[@id='buttonFinish']/i").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
