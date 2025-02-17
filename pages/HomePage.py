import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.PageBase import PageBase
from constants.homepageconstants import *

@pytest.mark.usefixtures("HomePagesetup")
class Homepage(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def get_title(self):
        return self.driver.title
    
    def click_navbar_company(self):
        navbarcompany = self.wait_element_visibility(NAVBAR_COMPANY_LOCATE)
        navbarcompany.click()
        
    def click_dropdown_career(self):
        dropdowncareer = self.wait_element_visibility(DROPDOWN_CAREER_LOCATE)
        dropdowncareer.click()

    def is_teams_visible(self):
        return self.wait_element_visibility(TEAMS_LOCATE).is_displayed()
    
    def is_locations_visible(self):
        return self.wait_element_visibility(LOCATIONS_LOCATE).is_displayed()
    
    def is_life_at_insider_visible(self):
        return self.wait_element_visibility(LIFE_AT_INSIDER_LOCATE).is_displayed()
    
    def accept_cookies(self):
        self.wait_element_visibility(COOKIES_LOCATE).click()