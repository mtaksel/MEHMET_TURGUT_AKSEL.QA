from selenium.webdriver.common.by import By

QA_PAGE_BASE_URL = "https://useinsider.com/careers/quality-assurance/"

QA_PAGE_TITLE = "Insider quality assurance job opportunities"
COOKIES_LOCATE = (By.XPATH, "//a[@id='wt-cli-accept-all-btn']")
SEE_ALL_QA_JOBS_LOCATE = (By.XPATH, "//a[.='See all QA jobs']")

LOCATION_DROPDOWN_LOCATE = (By.ID, "select2-filter-by-location-container")
LOCATION_VALUE_LOCATE = (By.ID, "select2-filter-by-location-result-11jb-Istanbul, Turkiye")
CLICK_VALUE_LOCATE = (By.XPATH, "//li[contains(text(), 'Istanbul, Turkiye')]")

DEPARTMENT_DROPDOWN_LOCATE = (By.ID, "select2-filter-by-department-container")
CLICK_DEPARTMENT_LOCATE = (By.XPATH, "//li[contains(text(), 'Quality Assurance')]") 

JOB_DESCRIPTION_LOCATE = (By.XPATH,"//div[@id='jobs-list']/div[1]//span[@class='position-department text-large font-weight-600 text-primary']")
JOB_TEXT = "Quality Assurance"


LOCATION_DESCRIPTION_LOCATE = (By.XPATH,"//div[@id='jobs-list']/div[1]//div[@class='position-location text-large']")
LOCATION_TEXT = "Istanbul, Turkiye"

HOVER_LOCATE = (By.XPATH, "position-list-item-wrapper bg-light")
VIEW_ROLE_LOCATE = (By.XPATH, "//a[@href='https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc']")

NEW_TAB_JOB_NAME_LOCATE = (By.XPATH, "//h2[contains(text(), 'Senior Software Quality Assurance Engineer')]")
NEW_TAB_JOB_NAME_TEXT = "Senior Software Quality Assurance Engineer"

APPLY_BUTTON_LOCATE = (By.XPATH, "//div[@class='postings-btn-wrapper']/a[.='Apply for this job']")
APPLY_FORM_TITLE = "Insider. - Senior Software Quality Assurance Engineer"