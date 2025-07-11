from playwright.sync_api import Page, expect


def test_handle_webTable(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    riceRow=page.locator("tr").filter(has_text="Rice")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColumn=index
            print(f"price is present at {priceColumn}")
            break
    expect(riceRow.locator("td").nth(priceColumn)).to_have_text("37")
