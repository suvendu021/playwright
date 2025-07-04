from .dashboard import DashBoard


class Login:


    def __init__(self,page):
        self.page=page


    def navigate_to_website(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login_to_website(self,userName,passWord):
        self.page.get_by_placeholder("email@example.com").fill(userName)
        self.page.get_by_placeholder("enter your passsword").fill(passWord)
        self.page.get_by_role("button", name="Login").click()
        dashboard=DashBoard(self.page)
        return dashboard

