from src.utils.RestApiClient import RestApiClient
from src.config.EnvSettings import EnvSettings

class BasePet():
    client =  RestApiClient(EnvSettings().getEnvConfig()["baseurl"])
    path = 'v2/pet/'