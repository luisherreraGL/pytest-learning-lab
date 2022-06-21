import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from src.utils.BrowserActions import BrowserActions
from src.config.ConfigEnv import ConfigEnv

def pytest_addoption(parser):
    parser.addoption("--env", action = "store", help ="Define environment to execute test")

@pytest.fixture
def get_env(request):
    environment = request.config.getoption("--env")
    return environment

@pytest.fixture
def environment_config(get_env):
    config = ConfigEnv(get_env)
    return config


@pytest.fixture
def browserActions(environment_config):
    print("setup browserActions")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browserActions = BrowserActions(driver, environment_config.baseurl)
    yield browserActions
    print("teardown browserActions")
    driver.close()