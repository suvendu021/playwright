from .orderhistory import OrderHistory


class Order:

    def __init__(self,page):
        self.page=page

    def click_on_view_order(self,orderId):
        order = self.page.locator("tr").filter(has_text=orderId)
        order.get_by_role("button", name="View").click()
        orderHistory=OrderHistory(self.page)
        return orderHistory