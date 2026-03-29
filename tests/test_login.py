import pytest
from pages.login_page import LoginPage
from data.login_data import login_data

@pytest.mark.parametrize("username,password", login_data)
def test_valid_login(setup, username, password):
    driver = setup

    driver.get("https://the-internet.herokuapp.com/login")

    login = LoginPage(driver)
    login.login(username, password)

    assert "You logged into a secure area!" in login.get_success_message()