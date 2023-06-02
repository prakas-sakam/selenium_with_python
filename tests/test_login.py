import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from tests.conftest import strat_and_stop


@pytest.mark.usefixtures("strat_and_stop")
class TestLogin:
    def test_login_without_credentials(self):
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-user']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Login']']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").is_displayed()
    #       allure.attach(self.driver.get_screenshot_as_png(),name="test_login_without_credentials",attachment_type = AttachmentType.PNG)




    def test_login_credentials(self):
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-user']").click()
        self.driver.find_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("s.prakasreddy@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("0000000000")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        assert self.driver.find_element(By.XPATH, "//a[@class='list-group-item'][normalize-space()='Logout']").is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="test_login_without_credentials", attachment_type = AttachmentType.PNG)


