import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_Search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear() #Limpia en caso de haber texto

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        search_field.send_keys('seat shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1,len(products))
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main":
    unittest.main(verbosity=2)