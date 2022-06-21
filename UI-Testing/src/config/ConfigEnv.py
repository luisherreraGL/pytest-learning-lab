class ConfigEnv:
    SUPORTED_URLS = {
        'dev': 'https://demoblaze.com',
        'qa': 'https://docs.pytest.org'    
    }

    def __init__(self, env) -> None:
        environment = env or 'dev'
        self.baseurl = self.SUPORTED_URLS[environment]