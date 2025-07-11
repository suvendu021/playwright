from playwright.sync_api import Playwright, expect

from utils.api_helper import ApiHelper


def test_end2end_api_and_ui_testing(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    apiHelper_object = ApiHelper()
    orderId = apiHelper_object.createOrder(playwright)
    print(orderId)


    # login to website
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("suvendu.sahoo@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Suvendu@123")
    page.get_by_role("button",name="Login").click()
    expect(page.get_by_role("button",name=" HOME ")).to_be_visible()

    page.get_by_role("button",name="ORDERS").click()





    # go to order history > match with order id click view button
    order=page.locator("tr").filter(has_text=orderId)
    order.get_by_role("button",name="View").click()

    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")

    context.close()

