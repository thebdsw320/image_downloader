import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=('/usr/bin/chromedriver'))
        driver = self.driver
        driver.get('http://demo.onestepcheckout.com')
        driver.maximize_window()
        driver.implicitly_wait(15)
        
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('search')

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name('q')

    def test_search_text_field_by_class(self):
        search_field = self.driver.find_element_by_class_name('input-text')

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name('button')


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)