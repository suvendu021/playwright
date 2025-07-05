
import pytest

@pytest.fixture(scope="session")
def credential_of_user(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser type")



@pytest.fixture
def create_browser_object(playwright,request):
    browser_type=request.config.getoption("browser_name")
    if browser_type == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_type == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()