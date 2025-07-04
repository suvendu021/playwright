import time

from playwright.sync_api import Page, expect, Playwright


def test_login_page(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("leargggning")
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("button",name="Sign In").click()
    page.get_by_role("link",name="terms and conditions").click()
    page.locator("#terms").check()
    #Empty username/password.
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)

def test_login_in_firefox_engine(playwright:Playwright):
    browser=playwright.firefox.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("leargggning")
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    # Empty username/password.
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)


