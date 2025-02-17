from time import sleep
from selenium import webdriver
import softest
import unittest
import pytest
from constants.qajobspageconstants import *
from pages.QAJobsPage import QAPage
from pages.HomePage import *
from pages.PageBase import PageBase


@pytest.mark.usefixtures("QaPagesetup")
class TestQAPage(softest.TestCase, unittest.TestCase):
    
    #Go to https://useinsider.com/careers/quality-assurance/ and check the page title
    
    def test_verify_QAPage_title(self):
        qapage = QAPage(self.driver)
        qapage.accept_cookies()
        qapage.get_title()
        try:
            self.soft_assert(self.assertEqual,qapage.get_title(),QA_PAGE_TITLE, "The data is not matching")
            self.assert_all()
        except AssertionError as e:  
            print(f" Test failed: {str(e)}")
            self.driver.save_screenshot(r"images\qa_page_tite_not_matching.png")
    
    #Go to https://useinsider.com/careers/quality-assurance/, click “See all QA jobs”, filter
    #jobs by Location: “Istanbul, Turkey”, and Department: “Quality Assurance”, check the presence of the job list
    
    def test_check_qa_jobs_filter(self):
        qapage = QAPage(self.driver)
        qapage.accept_cookies()
        qapage.click_see_all_qa_jobs()
        qapage.click_location_dropdown()
        qapage.click_location_value()
        qapage.click_department_dropdown()
        qapage.click_department_value()
        qapage.scroll_down()

    ##Check that all jobs’ Position contains “Quality Assurance”, Department contains
    #“Quality Assurance”, and Location contains “Istanbul, Turkey”

        try:
            self.soft_assert(self.assertEqual, qapage.verify_department(), JOB_TEXT, "The data is not matching")
            self.soft_assert(self.assertEqual, qapage.verify_location(), LOCATION_TEXT, "The data is not matching")
            self.assert_all()
        except AssertionError as e:  
            print(f" Test failed: {str(e)}")
            self.driver.save_screenshot(r"images\job_location_department_not_matching.png")
        sleep(2)


    #Click the “View Role” button and check that this action redirects us to the Lever Application form page

    def test_check_view_role_button(self):
        qapage = QAPage(self.driver)
        qapage.accept_cookies()
        qapage.click_see_all_qa_jobs()
        qapage.click_location_dropdown()
        qapage.click_location_value()
        qapage.click_department_dropdown()
        qapage.click_department_value()
        qapage.scroll_down()

        try:
            self.soft_assert(self.assertEqual, qapage.verify_department(), JOB_TEXT, "The data is not matching")
            self.soft_assert(self.assertEqual, qapage.verify_location(), LOCATION_TEXT, "The data is not matching")
            self.assert_all()
        except AssertionError as e:  
            print(f" Test failed: {str(e)}")
            self.driver.save_screenshot(r"images\job_location_department_not_matching.png")

        qapage.hover_on_job()
        qapage.click_view_role()
        qapage.switch_to_new_tab()

        try:
            self.soft_assert(self.assertEqual, qapage.verify_new_tab_job_name(), NEW_TAB_JOB_NAME_TEXT, "The data is not matching")
            self.assert_all()
        except AssertionError as e:  
            print(f" Test failed: {str(e)}")
            self.driver.save_screenshot(r"images\new_tab_job_name_errors.png")

        qapage.click_apply_button()

        try:
            self.soft_assert(self.assertEqual, qapage.get_title(),APPLY_FORM_TITLE, "The data is not matching")
            self.assert_all()
        except AssertionError as e:  
            print(f" Test failed: {str(e)}")
            self.driver.save_screenshot(r"images\apply_form_title_errors.png")

        
