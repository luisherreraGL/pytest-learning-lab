import pytest
from src.utils.RestApiClient import RestApiClient
from src.dataGenerators.PetDataGenerator import PetDataGenerator
from src.config.SettingsEnv import SettingsEnv

def pytest_html_report_title(report):
    report.title = "API Testing Report"

@pytest.fixture(scope="session")
def environment_config():
    return SettingsEnv().getEnvConfig()

@pytest.fixture
def baseURL(environment_config):
    return environment_config["baseurl"]

@pytest.fixture
def insertedNewPet(baseURL):
    client = RestApiClient(baseURL)
    payloadJson = PetDataGenerator().getNewPet()
    response = client.post( 'v2/pet', payloadJson).assertStatus(200).getJson()
    return response
