from selenium.webdriver.common.by import By

HOME_PAGE_BASE_URL = "https://useinsider.com"

##

HOMEPAGE_TITLE = "#1 Leader in Individualized, Cross-Channel CX — Insider"
NAVBAR_COMPANY_LOCATE = (By.XPATH, "//a[contains(.,'Company')]")
DROPDOWN_CAREER_LOCATE = (By.XPATH, "//a[.='Careers']")
TEAMS_LOCATE = (By.XPATH, "//a[.='See all teams']")
LOCATIONS_LOCATE = (By.XPATH, "//h3[@class='category-title-media ml-0']")
LIFE_AT_INSIDER_LOCATE = (By.XPATH, "//h2[.='Life at Insider']")
COOKIES_LOCATE = (By.XPATH, "//a[@id='wt-cli-accept-all-btn']")