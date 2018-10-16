from selenium import webdriver
import unittest


class EnvSetup(unittest.TestCase):
    def setUp(self, driver):
        self.driver = webdriver.Chrome('C:\Personal\HTML-CSS\Python\chromedriver.exe')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

