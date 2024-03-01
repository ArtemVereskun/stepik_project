import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Specify the language for tests")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
