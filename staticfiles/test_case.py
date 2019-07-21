import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EFS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def EFS_login_add_investment_test(self):
        # Login credentials
        user = "Admin"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        # Navigate to the login page and enter credentials
        driver.get("http://127.0.0.1:8000/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        # Click on the 'login' button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]").click()
        time.sleep(2)
        assert "Logged In"
        # Navigate to "Investments" (click on 'View Details')
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(2)
        # Click on 'Add Investment'
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)
        # Fill out the required fields for a new service
        elem = driver.find_element_by_id("id_customer")
        elem.send_keys("50712")
        elem = driver.find_element_by_id("id_category")
        elem.send_keys("Selenium Test")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("Test with Selenium")
        elem = driver.find_element_by_id("id_acquired_value")
        elem.send_keys("1500")
        elem = driver.find_element_by_id("id_acquired_date")
        elem.send_keys("")
        elem = driver.find_element_by_id("id_recent_value")
        elem.send_keys("1600")
        elem = driver.find_element_by_id("id_recent_date")
        elem.send_keys("")
        time.sleep(2)
        # Click the 'Save' button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)
        assert "Posted MFS Entry"
        # Return to the homepage and close the program
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()