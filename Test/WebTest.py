from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
sys.path.append('C:/Users/Va185060/PycharmProjects/PythonTest')
from pageObjects.LognPage import loginPage

class OrangeTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver= webdriver.Chrome(executable_path="C:/Users/Va185060/Desktop/sag/chromedriver.exe")
        cls.driver.maximize_window()



    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM",self.driver.title,"Login titile is not matching")


    def test_Filllogin(self):
        lp=loginPage(self.driver)
        self.driver.save_screenshot('./Screenshots/login.png')
        lp.setuser('admin')
        lp.setPSW('admin123')
        self.driver.save_screenshot('./Screenshots/BeforeClick.png')
        lp.clickBT()
        self.driver.save_screenshot('./Screenshots/HomePage.png')
        self.assertEqual("OrangeHRM",self.driver.title,"Login titile is not matching")



    @classmethod
    def tearDown(self):
        self.driver.quit()
        print("Testing completed")


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner("./Reports"))

