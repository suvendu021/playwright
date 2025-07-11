import time
from playwright.sync_api import Page, expect

def intercepting_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6863642c129e250258c33f59")

def test_api_request_intercept(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("suvendu.sahoo@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Suvendu@123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("button", name=" HOME ")).to_be_visible()

    # Set up route interception
    page.route(
        "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",
        intercepting_request
    )

    # Click on Orders and View
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()

    # time.sleep(3)
    # Get and print the message
    message = page.locator(".blink_me").text_content()
    print(message)
