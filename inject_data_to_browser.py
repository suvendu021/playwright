from playwright.sync_api import Playwright, expect
from utils.api_helper import ApiHelper


def test_inject_data_to_browser(playwright:Playwright):
    apiHelper = ApiHelper()
    token = apiHelper.getToken(playwright)

    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()




    page.add_init_script(f"""localStorage.setItem("token", "{token}")""")


    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button",name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()