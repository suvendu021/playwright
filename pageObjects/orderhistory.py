from playwright.sync_api import expect


class OrderHistory:
    def __init__(self,page):
        self.page=page

    def validate_order_history_page(self):
        expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
