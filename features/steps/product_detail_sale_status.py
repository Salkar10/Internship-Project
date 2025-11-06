
from time import sleep
from behave import given, when, then
from pages.login_page import LoginPage
from pages.off_plan_page import OffPlanPage
import time


@given('I am on the main page "{url}"')
def step_open_main_page(context, url):
    """Open the main page"""
    context.app.login_page.open_login_page(url)
    time.sleep(2)  # Wait for page to load


@when('I log in to the page')
def step_login(context):
    """Log in to the page"""
    context.app.login_page.user_login('salahmechou10@outlook.com', 'Salah1992.')
    print("Login successful")

@when('I click on "off plan" in the left side menu')
def step_click_off_plan(context):
    """Click on off plan menu"""
    time.sleep(10)  # Wait for page to load
    context.app.off_plan_page.click_off_plan_menu()
    time.sleep(5)

    print("Clicked on off plan menu")

@when('I check the sale status of the first product')
def step_check_first_product_sale_status(context):
    """Check and store the sale status of the first product"""
    sleep(10)
    #context.app.off_plan_page.get_first_product_sale_status.text()
    context.expected_sale_status = context.app.off_plan_page.get_first_product_sale_status()
    #wait for off plan product list to load before reading status
    print(f"First product sale status: {context.expected_sale_status}")


@when('I click the first product')
def step_click_first_product(context):
    """Click on the first product"""
    context.app.off_plan_page.click_first_product()
    # Wait for product detail page to load
    time.sleep(5)
    #off_plan_page.click_first_product()
    print("Clicked on first product")


@then('I verify that in the Details section, the sale status is correct')
def verify_first_product_sale_check_status(context):
    """Verify the sale status in Details section matches the expected status"""
    time.sleep(5)
    context.actual_sale_status = context.app.off_plan_page.verify_first_product_sale_check_status()
    print(f"First product sale status: {context.expected_sale_status}")
    print(f'Actual status: {context.actual_sale_status}')
    assert context.expected_sale_status == context.actual_sale_status, f'Expected sale status: {context.expected_sale_status} != {context.actual_sale_status}'
    print("✓ Sale status verification successful!")