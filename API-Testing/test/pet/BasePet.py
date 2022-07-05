from src.utils.RestApiClient import RestApiClient
from src.config.ApiConfig import credentials
from src.config.SettingsEnv import SettingsEnv
import pytest
class BasePet():
    client =  RestApiClient(SettingsEnv().getEnvConfig()["baseurl"])
    path = 'v2/pet/'

    @pytest.fixture(autouse=True)
    def setAuth(self):
        self.client.addDefaultHeaders({"api_key": credentials["api_key"]})
