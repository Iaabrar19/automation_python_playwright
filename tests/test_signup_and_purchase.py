from pages.signup_page import SignupPage
from pages.product_page import ProductPage, contact_us, checkout

def test_signup_and_purchase(page):
    signup = SignupPage(page)
    signup.signup()
    signup.fill_account_info()
    signup.logout()

    product_page = ProductPage(page)
    product_page.browse_and_add_product()
    
        # Proceed to checkout
    checkout(page)

    # Optionally, contact us page test
    contact_us(page)

