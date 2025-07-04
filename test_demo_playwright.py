from playwright.sync_api import Page

def test_demo_playwright(playwright):
    browser=playwright.chromium.launch(headless=False) # return browser object
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com")

def testdemo_shortcut(page:Page):
     page.goto("https://rahulshettyacademy.com")