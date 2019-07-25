import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MFS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_MFS(self):
        # Login credentials
        user = "Test"
        pwd = "test123"
        driver = self.driver
        driver.maximize_window()
        # Navigate to the login page and enter credentials
        driver.get("http://127.0.0.1:8000/accounts/login/")
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
        # Navigate to "Services" (click on 'View Details')
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(2)
        # Click on 'Add Service'
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)
        # Fill out the required fields for a new service
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Barbara York")
        elem = driver.find_element_by_id("id_service_category")
        elem.send_keys("Food Prep/Delivery")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("Test with Selenium")
        elem = driver.find_element_by_id("id_location")
        elem.send_keys("PKI Test")
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys("15")
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