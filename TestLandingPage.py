from EnvSetupFile import EnvSetup
from LandingPage import LandingPage
import unittest


class TestLandingPage(EnvSetup):

    def test_home_page(self):
        self.driver.get('http://wwww.automationpractice.com')

    lp = LandingPage()
    lp.click_sign_in()


if __name__ == '__main__':
    unittest.main()

    