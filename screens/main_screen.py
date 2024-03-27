from screens.base_screen import BaseScreen




main_pg_title:str = "//*[contains(text(),\"All-in-one\")]"
main_pg_login_btn:str = "//a[@id=\"signin\"]"

class MainScreen(BaseScreen):
    def main_title_is_exist(self):
       if self.is_element_exist(main_pg_title):
           return True
       else:
        return False

    def click_on_login_btn(self):
        self.click(main_pg_login_btn)
