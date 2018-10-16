from EnvSetupFile import EnvSetup
from selenium import webdriver
from selenium.webdriver.common.by import By


class LandingPage(EnvSetup):

    def __init__(self):
        self.driver = driver

        #self.sign_in = driver.find_element(By.CLASS_NAME, 'login')
        sign_in = self.driver.find_element(By.CLASS_NAME, 'login')

    def click_sign_in(self, driver):
        self.sign_in.click()

