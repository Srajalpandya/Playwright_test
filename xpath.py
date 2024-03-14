from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #relative xpath '//'
    #Using Attribute - '//tagname[@attibutename = "value"]'
    # username_element = page.wait_for_selector('//input[@name = "username"]')
    # password_element = page.wait_for_selector('//input[@name = "password"]')
    # button_click = page.wait_for_selector('//button[@type = "submit"]')
    #
    # username_element.type("Admin")
    # password_element.type("admin123")
    # button_click.click()
    # page.wait_for_timeout(3000)

    # text - '//tagname[text() = "text"]'

    forgot_password = page.wait_for_selector("//p[text() = 'Forgot your password? ']")
    forgot_password.click()
    page.wait_for_timeout(3000)


    #contains
    #attributes - //tagname[contains(@attributes, "Values")]
    # //input[contains(@placeholder, "user")]
    #text - //tagname[containes(text(), "value")]
    # -> //label[contains(text(), "username")]

    #dynamic - Srajal , SrajalP, SrajaPandya
    #Start-with  - //tagname[start-with(@id,"Srajal")]
    #End-with  - //tagname[End-with(@id, "Pandya")]


    #family
    #parent - //tagname[@id = "value"]/parent :: input[]
    #child - //tagname[@id = "value"]/child :: input[]
    #ancestor -
    #sibling - //td[text()="Microsoft"]//following-sibling::tag[2]