from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.automationtesting.in/Selectable.html")

        #store multiple element using list
        elements = page.query_selector_all('b')
        print(len(elements))
        for i in elements:
            print(i.text_content())
        page.wait_for_timeout(5000)
    except Exception as e:
        print(str(e))
    finally:
        print("Execute")


