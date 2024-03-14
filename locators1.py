from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
#     page.goto("https://demo.automationtesting.in/Index.html")
#
# # Using CSS selector  id - # , class - . , attribute - tagname(attribute = "value")
#
# # Using id
#     emailtxtbox = page.wait_for_selector("#email")
#     emailtxtbox.type("luffy@gmail.com")
#     button = page.wait_for_selector("#enterimg")
#     button.click()
#     page.wait_for_timeout(3000)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #attribute
    #tagname[attibute = 'value']
    username = page.wait_for_selector('input[name = "username"]')
    username.type("Admin")
    password = page.wait_for_selector("input[name = 'password']")
    password.type("admin123")
    button = page.wait_for_selector('button[type = "submit"]')
    button.click()
    page.wait_for_timeout(3000)