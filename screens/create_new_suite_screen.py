from screens.base_screen import BaseScreen


class SuiteScreen(BaseScreen):
    trs_pay_tc_btn: str = "//*[contains(text(), \"TrastPay\")]"
    cr_suite_btn: str = "//a[@id=\"create-suite-button\"]"
    suite_name_input_fld: str = "//input[@class=\"DcqLJ3\"]"
    confirm_create_btn: str = "//button[@type=\"submit\"]//*[contains(text(), \"Create\")]"
    created_success_msg: str = "//*[contains(text(), \"Suite was successfully created.\")]"
    suite_title_btn: str = f"//*[@title=\"titeleName\"]"
    delete_icon: str = "//*[@data-icon=\"trash\"]"
    confirm_delete_btn: str = "//*[contains(text(),\"Delete\")]"
    deleted_success_msg: str = "//*[contains(text(), \"Suite was successfully deleted.\")]"

    def click_tc_title(self):
        self.click(self.trs_pay_tc_btn)

    def click_cr_suite_btn(self):
        self.click(self.cr_suite_btn)

    # def enter_suite_name(self, suite_name: str):
    #     self.enter_data(self.suite_name_input_fld, suite_name)
    #     self.suite_title_btn = f"//*[@title=\"{suite_name}\"]"

    def click_create_confirm_btn(self):
        self.click(self.confirm_create_btn)

    def is_created_msg_exist(self):
        if self.is_element_exist(self.created_success_msg):
            return True
        else:
            return False

    def click_created_suite_title(self):
        self.click(self.suite_title_btn)

    def click_delete_icon(self):
        self.click(self.delete_icon)

    def click_confirm_delete_btn(self):
            self.click(self.confirm_delete_btn)

    def is_deleted_msg_exist(self):
        if self.is_element_exist(self.deleted_success_msg):
            return True
        else:
            return False

    """taking Data from new page"""
    def switching_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def open_a_new_tab(self):
        self.driver.execute_script("window.open()")

    def navigate_to_new_opened_tab(self, url_link):
        self.open_a_new_tab()
        self.switching_to_new_window()
        self.driver.get(url_link)

    def return_to_main_tab_with_close(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


