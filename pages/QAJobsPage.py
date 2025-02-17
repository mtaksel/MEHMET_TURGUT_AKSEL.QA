import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.PageBase import PageBase
from constants.homepageconstants import *
from constants.qajobspageconstants import *
from pages.HomePage import *




@pytest.mark.usefixtures("QaPagesetup")
class QAPage(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_see_all_qa_jobs(self):
        see_all_qa_jobs = self.wait_element_visibility(SEE_ALL_QA_JOBS_LOCATE)
        see_all_qa_jobs.click()

    def accept_cookies(self):
        self.wait_element_visibility(COOKIES_LOCATE).click()
    
    def click_location_dropdown(self):
        sleep(4)
        location_filter = self.wait_element_visibility(LOCATION_DROPDOWN_LOCATE)
        location_filter.click()

    def click_location_value(self):
        sleep(2)
        location_click = self.wait_element_visibility(CLICK_VALUE_LOCATE)
        location_click.click()

    def click_department_dropdown(self):
        department_filter = self.wait_element_visibility(DEPARTMENT_DROPDOWN_LOCATE)
        department_filter.click()
    
    def click_department_value(self):
        department_click = self.wait_element_visibility(CLICK_DEPARTMENT_LOCATE)
        department_click.click()
        sleep(2)

    def verify_department(self):
        job_description = self.wait_element_visibility(JOB_DESCRIPTION_LOCATE)
        return job_description.text
    
    def verify_location(self):
        location_description = self.wait_element_visibility(LOCATION_DESCRIPTION_LOCATE)
        sleep(2)
        return location_description.text
        
    
    def hover_on_job(self):
        element_to_hover_over = self.wait_element_visibility(LOCATION_DESCRIPTION_LOCATE)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        sleep(2)
    
    def click_view_role(self):
        view_role = self.wait_element_visibility(VIEW_ROLE_LOCATE)
        view_role.click()
        sleep(2)

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def verify_new_tab_job_name(self):
        new_tab_job_name = self.wait_element_visibility(NEW_TAB_JOB_NAME_LOCATE)
        return new_tab_job_name.text
    
    def click_apply_button(self):
        apply_button = self.wait_element_visibility(APPLY_BUTTON_LOCATE)
        apply_button.click()
    
    def get_title(self):
        return self.driver.title