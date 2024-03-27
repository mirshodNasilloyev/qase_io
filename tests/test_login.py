from tests.test_base import BaseTest


class TestLogin(BaseTest):
    user_email = "mnasilloyev.ios@gmail.com"
    user_password = "@Nasilloyev96"
    low_psw = "123"
    name = "mark_manson"

    def test_main(self, init_chrome_driver):
        assert self.m_a.check_main_action()

    def test_login(self, init_chrome_driver):
        assert self.l_a.check_1login_action_negative("usa.damit@gmail.com", "ndsini238582@M")
        assert self.l_a.check_wrong_password(self.user_email, self.low_psw)
        assert self.l_a.check_login_action_positive(self.user_email, self.user_password)

    def test_suite_create_and_delete(self, init_chrome_driver):
        assert self.s_a.check_suite_created(self.name)

