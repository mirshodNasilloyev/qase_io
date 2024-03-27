import time
from screens.login_screen import LoginScreen


# from screens.create_new_suite_screen import SuiteScreen

class LoginAction(LoginScreen):

    def check_1login_action_negative(self, work_email, password):
        assert self.is_login_page_open()
        self.enter_email_address(work_email)
        self.enter_password(password)
        self.unmark_remember_btn()
        self.click_on_sign_in_btn()
        assert self.check_wrong_attempt_message()
        time.sleep(2)
        self.clear_login_and_password_fld()
        return True

    def check_wrong_password(self, work_email, wrong_psw):
        assert self.is_login_page_open()
        self.enter_email_address(work_email)
        self.enter_password(wrong_psw)
        self.click_on_sign_in_btn()
        self.is_wrong_psw_message_is_exist()
        time.sleep(2)
        assert self.is_reset_psw_pg_exist()
        self.click_back_button()
        time.sleep(2)
        return True

    def check_login_action_positive(self, work_email, password):
        assert self.is_login_page_open()
        self.enter_email_address(work_email)
        self.enter_password(password)
        # assert self.unmark_remember_btn()
        self.click_on_sign_in_btn()
        time.sleep(2)
        assert self.is_prj_page_open()
        time.sleep(2)
        return True
