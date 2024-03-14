from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.redbus.in/")

    #give all cookies
    my_cookies = page.context.cookies()
    print(my_cookies)

    #clear all the cookies
    page.context.clear_cookies()

    new_cookies = {
        'name' : 'Srajal',
        'IdUd' : '0235060863468468'
    }

    #To pass the new cookie of the page
    #page.context.add_cookies([new_cookies])

    #taking screenshots:
    page.screenshot(path='Test.png',full_page=True)
