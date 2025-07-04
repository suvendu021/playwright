from playwright.sync_api import Page

def test_child_window_from_parent_window(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")


    with page.expect_popup() as newPage:
        page.locator(".blinkingText").filter(has_text="Free Access to InterviewQues/ResumeAssistance/Material").click()
        childPage= newPage.value
        mail=childPage.get_by_role("link",name="mentor@rahulshettyacademy.com").text_content()
        print(mail)





