from src.utils.RestApiClient import RestApiClient
from src.config.ApiConfig import credentials
from src.config.EnvSettings import EnvSettings
import pytest
class BasePet():
    client =  RestApiClient(EnvSettings().getEnvConfig()["baseurl"])
    path = 'v2/pet/'

    @pytest.fixture(autouse=True)
    def setAuth(self):
        self.client.addDefaultHeaders({"api_key": credentials["api_key"]})
