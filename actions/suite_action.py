import time
from screens.create_new_suite_screen import SuiteScreen


class SuiteAction(SuiteScreen):

    def check_correct_data_took(self):
        self.navigate_to_new_opened_tab("https://translate.google.com/")
        time.sleep(5)
        self.return_to_main_tab_with_close()
        return True

    def check_suite_created(self):
        self.click_tc_title()
        self.click_cr_suite_btn()
        # self.enter_suite_name()
        self.click_create_confirm_btn()
        assert self.is_created_msg_exist()
        self.click_created_suite_title()
        self.click_delete_icon()
        self.click_confirm_delete_btn()
        assert self.is_deleted_msg_exist()
        time.sleep(2)
        return True