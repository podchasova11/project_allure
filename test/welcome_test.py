import allure

from examples_allure_pytest import get_message


def test_examples_allure_pytest():
    with allure.step("Welcome to Allure Report!"):
        assert get_message() == "Hello from examples.allure-pytest!"
