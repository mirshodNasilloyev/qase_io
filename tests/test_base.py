import pytest
from actions.main_action import MainAction
from actions.login_action import LoginAction
from actions.suite_action import SuiteAction


@pytest.mark.usefixtures("initialize_chromedriver", "get_screenshot_on_failed_case")
class BaseTest:

    @pytest.fixture
    def init_chrome_driver(self):
        driver = self.driver
        self.m_a = MainAction(driver)
        self.l_a = LoginAction(driver)
        self.s_a = SuiteAction(driver)
