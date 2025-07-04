from playwright.sync_api import expect

from .order import Order


class DashBoard:

    def __init__(self,page):
        self.page=page

    def validate_dashboard_page(self):
        expect(self.page.get_by_role("button", name=" HOME ")).to_be_visible()

    def navigate_to_order_page(self):
        self.page.get_by_role("button", name="ORDERS").click()
        order=Order(self.page)
        return order

