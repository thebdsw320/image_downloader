import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def tearDown(self):
        self.driver.quit()


if __name__ ==  "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='helloworldrep'))