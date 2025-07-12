from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1500)
    context = browser.new_context()
    page = context.new_page()

    # Visit login page
    page.goto("https://automationexercise.com/login")

    # Fill signup form
    name = "Ismail Aabrar"
    email = "ismailAabrar19919@example.com"

    page.locator('[data-qa="signup-name"]').fill(name)
    assert page.locator('[data-qa="signup-name"]').input_value() == name

    page.locator('[data-qa="signup-email"]').fill(email)
    assert page.locator('[data-qa="signup-email"]').input_value() == email

    page.locator('[data-qa="signup-button"]').click()

    # Gender
    page.locator("#id_gender1").click()

    # Account info
    page.locator('[data-qa="name"]').fill("IsmailAabrar")
    page.locator('[data-qa="password"]').fill("Aabrar123")
    page.locator('[data-qa="days"]').select_option("12")
    page.locator('[data-qa="months"]').select_option(label="October")
    page.locator('[data-qa="years"]').select_option("2005")

    page.locator("#newsletter").check()
    page.locator("#optin").check()

    page.locator('[data-qa="first_name"]').fill("John")
    page.locator('[data-qa="last_name"]').fill("Doe")
    page.locator('[data-qa="address"]').fill("123 Main St")
    page.locator('[data-qa="state"]').fill("California")
    page.locator('[data-qa="city"]').fill("Los Angeles")
    page.locator('[data-qa="zipcode"]').fill("90001")
    page.locator('[data-qa="mobile_number"]').fill("1234567890")

    page.locator('[data-qa="create-account"]').click()

    # Continue to next page
    page.locator('[data-qa="continue-button"]').click()

    # Go to products
    page.goto("https://automationexercise.com/products")

    # Expand Men category
    page.locator(':nth-child(2) > .panel-heading > .panel-title > a > .badge > .fa').click()

    # Click Men subcategory (2nd link)
    page.locator('#Men > .panel-body > ul > :nth-child(2) > a').click()

    # Click 3rd product's view link
    page.locator(':nth-child(3) > .product-image-wrapper > .choose > .nav > li > a').click()

    # Update quantity
    quantity_input = page.locator("#quantity")
    quantity_input.fill("")
    quantity_input.type("2")

    # Add to Cart
    page.locator(':nth-child(5) > .btn').click()

    # View Cart
    page.locator("u").first.click()

    # Proceed to checkout
    page.locator('.col-sm-6 > .btn').click()
    page.locator(':nth-child(7) > .btn').click()

    # Payment info
    page.locator('[data-qa="name-on-card"]').fill("aa")
    page.locator('[data-qa="card-number"]').fill("123")
    page.locator('[data-qa="cvc"]').fill("01")
    page.locator('[data-qa="expiry-month"]').fill("12")
    page.locator('[data-qa="expiry-year"]').fill("1999")

    page.locator('[data-qa="pay-button"]').click()

    # Contact Us page
    page.locator(':nth-child(9) > a').click()

    # Contact form
    page.locator('[data-qa="name"]').fill("aab")
    page.locator('[data-qa="email"]').fill("a@gmail.com")
    page.locator('[data-qa="subject"]').fill("h")
    page.locator('[data-qa="message"]').fill("adsasdsadsad")

    # File upload (make sure 'file.txt' exists)
    page.locator(':nth-child(6) > .form-control').set_input_files("file.txt")

    # Submit form
    page.locator('[data-qa="submit-button"]').click()

    browser.close()
