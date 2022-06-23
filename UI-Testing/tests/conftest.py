import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from src.utils.BrowserActions import BrowserActions
from src.config.ConfigEnv import ConfigEnv

def pytest_addoption(parser):
    parser.addoption("--env", 
        action="store",
        default="dev",
        choices=("dev", "qa"),
        help ="Define environment to execute test")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def environment_config(env):
    return ConfigEnv(env)

@pytest.fixture
def browserActions(environment_config):
    print("setup browserActions")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browserActions = BrowserActions(driver, environment_config.baseurl)
    yield browserActions
    print("teardown browserActions")
    driver.close()

