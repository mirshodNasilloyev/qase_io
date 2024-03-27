import time
from screens.base_screen import BaseScreen


class LoginScreen(BaseScreen):
    page_title = "//*[contains(text(), \"your account\")]"
    reset_psw_pg:str = "//*[@class=\"ilHPl4\"]"
    work_email_input_field = "//*[@placeholder='Work email']"
    password_input_field = "//*[@placeholder='Password']"
    sign_in_btn = "//*[text()=\"Sign in\"]"
    project_page_title = "//h1[text()='Projects']"
    milestone_column = "//tr[\"{}\"]/td[6]"
    wrong_attempt_msg = "//*[text()=\"These credentials do not match our records.\"]"
    low_psw_mg:str = "//*[@class=\"xtWHgv\"]"
    remember_me_btn_on: str = "//*[@class=\"jMrRsi mXgUdp\"]"
    remember_me_btn_off: str = "//*[@class=\"jMrRsi\"]"

    def is_login_page_open(self):
        if self.is_element_exist(self.page_title):
            return True
        else:
            return False

    def is_prj_page_open(self):
        if self.is_element_exist(self.project_page_title):
            return True
        else:
            return False

    def is_wrong_psw_message_is_exist(self):
        if self.is_element_exist(self.low_psw_mg):
            return True
        else:
            return False

    def is_reset_psw_pg_exist(self):
        if self.is_element_exist(self.reset_psw_pg):
            return True
        else:
            return False

    def check_wrong_attempt_message(self):
        if self.is_element_exist(self.wrong_attempt_msg):
            return True
        else:
            return False

    def enter_email_address(self, work_email):
        self.enter_data(self.work_email_input_field, work_email)

    def enter_password(self, password):
        self.enter_data(self.password_input_field, password)

    def click_on_sign_in_btn(self):
        self.click(self.sign_in_btn)

    def click_back_button(self):
        self.driver.back()

    def clear_login_and_password_fld(self):
        self.clear_input_field(self.work_email_input_field)
        time.sleep(2)
        self.clear_input_field(self.password_input_field)
    
    def unmark_remember_btn(self) -> bool:
        if self.is_element_exist(self.remember_me_btn_on):
            self.click(self.remember_me_btn_on)
            return True
        elif self.is_element_exist(self.remember_me_btn_off):
            self.click(self.remember_me_btn_off)
            return True
        else:
            return False
        