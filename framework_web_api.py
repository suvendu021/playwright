import json

import pytest
from playwright.sync_api import Playwright

from pageObjects.login import Login
from utils.api_helper import ApiHelper



with open("data_for_framework/credentials.json") as f:
    credentials_data=json.load(f)
    credential_list=credentials_data["credentials"]


@pytest.mark.smoke
@pytest.mark.parametrize('credential_of_user',credential_list)
def test_end2end_api_and_ui_testing(playwright:Playwright,credential_of_user,create_browser_object):


    apiHelper_object = ApiHelper()
    orderId = apiHelper_object.createOrder(playwright,credential_of_user)
    # print(orderId)

    userName=credential_of_user["username"]
    passWord=credential_of_user["password"]


    # login to website

    login=Login(create_browser_object)
    login.navigate_to_website()
    dashboard=login.login_to_website(userName,passWord)

    # validate dashboard page
    dashboard.validate_dashboard_page()
    order=dashboard.navigate_to_order_page()

    # go to order history > match with order id click view button
    orderHistory=order.click_on_view_order(orderId)

    orderHistory.validate_order_history_page()


