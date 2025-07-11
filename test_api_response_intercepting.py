from playwright.sync_api import Page, expect



fake_response={"data":[],"message":"No Orders"}

def intercepting_response(route):
    route.fulfill(
        json=fake_response
    )



def test_api_response_intercept(page:Page):

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("suvendu.sahoo@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Suvendu@123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("button", name=" HOME ")).to_be_visible()
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercepting_response)
    page.get_by_role("button", name="ORDERS").click()
    expect(page.locator(".mt-4")).to_contain_text("You have No Orders to show at this time")
