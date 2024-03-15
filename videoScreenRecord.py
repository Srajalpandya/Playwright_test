from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir='.//videos')
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_selector("//input[@placeholder='Username']").fill("Admin")
    page.wait_for_selector("//input[@placeholder='Password']").fill("admin123")
    page.wait_for_timeout(3000)
    page.wait_for_selector("//button[@type='submit']").click()
    page.wait_for_timeout(3000)
    context.close()