import time
from screens.create_new_suite_screen import SuiteScreen


class SuiteAction(SuiteScreen):

    def check_suite_created(self, name):
        self.click_tc_title()
        time.sleep(10)
        self.click_cr_suite_btn()
        time.sleep(2)
        self.enter_suite_name(name)
        time.sleep(2)
        self.click_create_confirm_btn()
        time.sleep(5)
        assert self.is_created_msg_exist()
        time.sleep(5)
        self.click_created_suite_title()
        time.sleep(2)
        self.click_delete_icon()
        time.sleep(2)
        self.click_confirm_delete_btn()
        time.sleep(1)
        assert self.is_deleted_msg_exist()
        time.sleep(5)
        return True