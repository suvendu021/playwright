import time

from playwright.sync_api import Page, expect


def test_for_handle_dialog(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.on("dialog",lambda dialog:dialog.accept())
    page.get_by_role("button",name="Alert").click()
    time.sleep(6)

    pageFrame=page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    expect(pageFrame.locator("h2").filter(has_text=" Happy Subscibers!")).to_be_visible()
    time.sleep(6)