from pages.login_page import LoginPage
from utils.config import BASE_URL

class ProductPage:
    def __init__(self, page):
        self.page = page

    def browse_and_add_product(self):
        login_page = LoginPage(self.page)
        login_page.login()

        self.page.goto(f"{BASE_URL}/products")
        self.page.locator(':nth-child(2) > .panel-heading > .panel-title > a > .badge > .fa').click()
        self.page.locator('#Men > .panel-body > ul > :nth-child(2) > a').click()
        self.page.locator(':nth-child(3) > .product-image-wrapper > .choose > .nav > li > a').click()
        quantity_input = self.page.locator("#quantity")
        quantity_input.fill("")
        quantity_input.type("2")
        self.page.locator(':nth-child(5) > .btn').click()
        self.page.locator("u").first.click()

def checkout(page):
    page.locator('.col-sm-6 > .btn').click()
    page.locator(':nth-child(7) > .btn').click()

    page.locator('[data-qa="name-on-card"]').fill("aa")
    page.locator('[data-qa="card-number"]').fill("123")
    page.locator('[data-qa="cvc"]').fill("01")
    page.locator('[data-qa="expiry-month"]').fill("12")
    page.locator('[data-qa="expiry-year"]').fill("1999")

    page.locator('[data-qa="pay-button"]').click()


def contact_us(page):
    page.locator(':nth-child(9) > a').click()

    page.locator('[data-qa="name"]').fill("aab")
    page.locator('[data-qa="email"]').fill("a@gmail.com")
    page.locator('[data-qa="subject"]').fill("h")
    page.locator('[data-qa="message"]').fill("adsasdsadsad")

    page.locator(':nth-child(6) > .form-control').set_input_files("file.txt")

    page.locator('[data-qa="submit-button"]').click()
