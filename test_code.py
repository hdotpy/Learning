from playwright.sync_api import Page, expect
import re


def test_saucedemo(page: Page):
    page.goto("https://www.saucedemo.com")
    expect(page).to_have_title(re.compile("Swag Labs", re.IGNORECASE))
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    inventory_item = page.locator(".inventory_item").all()
    for product in inventory_item:
        product_name = product.locator(
            ".inventory_item_name").text_content()
        product_price = product.locator(
            ".inventory_item_price").text_content()
        add_cart = product.locator("button:has-text('Add to cart')")
        if add_cart.is_visible():
            add_cart.click()
            print(
                f"{product_name} with its {product_price} is successfully added to cart")
        else:
            print(f"Add cart button is not enabled for {product_name}")

    shopping_cart_badge = page.locator(
        ".shopping_cart_badge")
    expect(shopping_cart_badge).to_have_text("6")
    page.wait_for_timeout(3000)
    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()
    page.locator("#first-name").fill("User")
    page.locator("#last-name").fill("Aware")
    page.get_by_placeholder("Zip/Postal Code").fill("123456")
    page.locator("#continue").click()
    page.locator("#finish").click()
    page.screenshot(path="full_page.png", full_page=True)
    thanks_message = page.get_by_test_id("complete-header")
    expect(thanks_message).to_have_text(re.compile(
        "Thank you for your order!", re.IGNORECASE))
