from src.utils.RestApiClient import RestApiClient
from src.config.ApiConfig import credentials
from src.config.SettingsEnv import SettingsEnv
import pytest
from src.assertions.CommonAssertions import CommonAssertions
class BasePet():
    client =  RestApiClient(SettingsEnv().getEnvConfig()["baseurl"])
    path = 'v2/pet/'
    commonAssertions = CommonAssertions()

    @pytest.fixture(autouse=True)
    def setAuth(self):
        self.client.addDefaultHeaders({"api_key": credentials["api_key"]})
