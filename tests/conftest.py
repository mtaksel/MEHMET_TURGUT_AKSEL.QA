from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest
from constants.homepageconstants import *
from constants.qajobspageconstants import *


@pytest.fixture(scope="function")
def HomePagesetup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(HOME_PAGE_BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def QaPagesetup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(QA_PAGE_BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
