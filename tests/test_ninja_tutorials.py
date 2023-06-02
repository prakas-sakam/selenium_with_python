import time
import pytest
from selenium.webdriver.common.by import By
from tests.conftest import strat_and_stop

@pytest.mark.usefixtures("strat_and_stop")
class TestNinja:
    def test_search_for_item(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("hp")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.XPATH, "//a[normalize-space()='HP LP3065']").is_displayed()
        time.sleep(3)



    def test_search_for_nothing(self):

        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("honda")
        expected_text = "There is no product that matches the search criteria."
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'There is no product that matches the search criter')]").text.__eq__(expected_text)
       # assert expected_text.__eq__(new.text)

        time.sleep(3)
#ninja = test_ninja()
