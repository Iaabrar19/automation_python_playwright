from utils.config import BASE_URL, TEST_USER

class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self):
        self.page.goto(f"{BASE_URL}/login")
        self.page.locator('xpath=//*[@id="form"]/div/div/div[1]/div/form/input[2]').fill(TEST_USER["email"])
        self.page.locator('xpath=//*[@id="form"]/div/div/div[1]/div/form/input[3]').fill(TEST_USER["password"])
        self.page.locator('xpath=//*[@id="form"]/div/div/div[1]/div/form/button').click()
