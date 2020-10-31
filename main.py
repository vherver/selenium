import unittest

from pyunitreport import HTMLTestRunner

from selenium import webdriver

class HelloWorld(unittest.TestCase):
	# Realiza todo lo necesario antes de empezar la prueba
    @classmethod # Decorador para que las distintas paginas corran en una sola pestaña
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
        driver = cls.driver
        driver.get('http://demo.onestepcheckout.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)


    def test_search_field(self):
        search_field = self.driver.find_element_by_id("search")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report') )