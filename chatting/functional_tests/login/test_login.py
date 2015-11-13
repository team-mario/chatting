from functional_tests.base import FunctionalTest


class LoginTest(FunctionalTest):
    def registration(self):
        self.browser.find_element_by_id('btn_register').click()
        self.browser.find_element_by_id('btn_registration').click()
        self.browser.find_element_by_id('id_username').send_keys("new_user")
        self.browser.find_element_by_id('id_email').send_keys('test@naver.com')
        self.browser.find_element_by_id('id_password1').send_keys('test')
        self.browser.find_element_by_id('id_password2').send_keys('test')
        self.browser.find_element_by_id('btn_registration').submit()

    def login(self):
        self.browser.find_element_by_id('btn_login').click()
        self.browser.find_element_by_id('id_username').send_keys('new_user')
        self.browser.find_element_by_id('id_password').send_keys('test')
        self.browser.find_element_by_id('btn_login').submit()

    def change_password(self):
        self.browser.find_element_by_id('btn_information').click()
        self.browser.find_element_by_id('btn_change_password').click()

        self.browser.find_element_by_id('id_old_password').send_keys('test')
        self.browser.find_element_by_id('id_new_password1').send_keys('test1')
        self.browser.find_element_by_id('id_new_password2').send_keys('test1')
        self.browser.find_element_by_id('btn_change_password_submit').click()

    def logout(self):
        self.browser.find_element_by_id('btn_information').click()
        self.browser.find_element_by_id('btn_logout').click()

    def limit_access_in_main_page(self):
        self.browser.get(self.live_server_url + '/issue/')
        # The anonymous user is redirected to login page.
        self.browser.find_element_by_id('btn_registration')

    def landing_page(self):
        logo = self.browser.find_element_by_id('logo')
        self.assertIn('/', logo.get_attribute('href'))

        btn_login = self.browser.find_element_by_id('btn_login')
        btn_register = self.browser.find_element_by_id('btn_register')

        self.assertIn('/accounts/login/', btn_login.get_attribute('href'))
        self.assertIn('/accounts/registration/', btn_register.get_attribute('href'))

    def test_login(self):
        self.landing_page()
        self.registration()
        self.login()
        self.change_password()
        self.logout()
        self.limit_access_in_main_page()
