from time import sleep
from selenium import webdriver
from pages.HomePage import *
import softest
import unittest
import pytest

@pytest.mark.usefixtures("HomePagesetup")
class TestHomePage(softest.TestCase, unittest.TestCase):
    
    #Visit https://useinsider.com/ and check Insider home page is opened or not
    
    def test_verify_homepage_title(self):
        homepage = Homepage(self.driver)
        homepage.accept_cookies()
        homepage.get_title()
        try:
            self.soft_assert(self.assertEqual,homepage.get_title(),HOMEPAGE_TITLE, "The data is not matching")
            self.assert_all()
        except AssertionError as e:  
            print(f" Test failed: {str(e)}")
            self.driver.save_screenshot(r"images\home_page_title_errors.png")

    #Select the “Company” menu in the navigation bar, select “Careers” and check Career page, its Locations, Teams, and Life at Insider blocks are open or not
    
    def test_check_career_page(self):
        homepage = Homepage(self.driver)
        homepage.accept_cookies()
        homepage.click_navbar_company()
        homepage.click_dropdown_career()
        homepage.scroll_down_to_bottom()
        try:
            self.soft_assert(self.assertTrue,homepage.is_teams_visible(), "The data is not matching")
            self.soft_assert(self.assertTrue,homepage.is_locations_visible(), "The data is not matching")
            self.soft_assert(self.assertTrue,homepage.is_life_at_insider_visible(), "The data is not matching")
            self.assert_all()
        except AssertionError as e:  
            print(f" Test failed: {str(e)}")
            self.driver.save_screenshot(r"images\homepage_blocks_errors.png")