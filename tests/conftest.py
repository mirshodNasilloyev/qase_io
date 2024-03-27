import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def get_screenshot_on_failed_case(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(request.instance.driver.get_screenshot_as_png(),
                      name="failed_test",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(params=["chrome"], scope="class")
def initialize_chromedriver(request):
    global driver
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        chrome_service = Service()
        request.cls.driver = webdriver.Chrome(options=options, service=chrome_service)
    request.cls.driver.maximize_window()
    request.cls.driver.get("https://qase.io")
    request.cls.driver.implicitly_wait(10)
    yield
    request.cls.driver.quit()
