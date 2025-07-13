from utils.config import BASE_URL, TEST_USER

class SignupPage:
    def __init__(self, page):
        self.page = page

    def signup(self):
        self.page.goto(f"{BASE_URL}/login")
        self.page.locator('[data-qa="signup-name"]').fill(TEST_USER["name"])
        self.page.locator('[data-qa="signup-email"]').fill(TEST_USER["email"])
        self.page.locator('[data-qa="signup-button"]').click()

    def fill_account_info(self):
        self.page.locator("#id_gender1").click()
        self.page.locator('[data-qa="name"]').fill(TEST_USER["name"])
        self.page.locator('[data-qa="password"]').fill(TEST_USER["password"])
        self.page.locator('[data-qa="days"]').select_option("12")
        self.page.locator('[data-qa="months"]').select_option(label="October")
        self.page.locator('[data-qa="years"]').select_option("2005")
        self.page.locator("#newsletter").check()
        self.page.locator("#optin").check()
        self.page.locator('[data-qa="first_name"]').fill(TEST_USER["first_name"])
        self.page.locator('[data-qa="last_name"]').fill(TEST_USER["last_name"])
        self.page.locator('[data-qa="address"]').fill(TEST_USER["address"])
        self.page.locator('[data-qa="state"]').fill(TEST_USER["state"])
        self.page.locator('[data-qa="city"]').fill(TEST_USER["city"])
        self.page.locator('[data-qa="zipcode"]').fill(TEST_USER["zipcode"])
        self.page.locator('[data-qa="mobile_number"]').fill(TEST_USER["mobile_number"])
        self.page.locator('[data-qa="create-account"]').click()
        self.page.locator('[data-qa="continue-button"]').click()

    def logout(self):
        with self.page.expect_navigation():
            self.page.locator('xpath=//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
