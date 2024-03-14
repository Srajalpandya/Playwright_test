from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Selectable.html")

#Mouse Actions Hover the dropdown
    page.wait_for_selector('//a[text()="SwitchTo"]').hover()

#Click on element
    page.wait_for_selector('//a[text()="SwitchTo"]').click()

#Double Click
    page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()

# Right on Element
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button="right")

#Shift Click
    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=["Shift"])

#Keyboard
    page.wait_for_selector('//a[text()="SwitchTo"]').press("A")
#Backquote, Minus, Equal, Backslash, Backspace, Tab, Delete, Escape,
#ArrowDown, End, Enter, Home, Insert, PageDown, PageUp, ArrowRight,
#ArrowUp, F1 - F12, Digit0 - Digit9, KeyA - KeyZ, etc.

    page.wait_for_selector('//a[text()="SwitchTo"]').press("$")