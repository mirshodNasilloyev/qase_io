from screens.main_screen import MainScreen


class MainAction(MainScreen):
    def check_main_action(self):
        assert self.main_title_is_exist(), "Main page title does not displayed"
        self.click_on_login_btn()
        return True