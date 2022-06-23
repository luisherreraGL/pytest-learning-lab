class ConfigEnv:
    SUPORTED_ENVS = ('qa', 'dev')
    SUPORTED_URLS = {
        'dev': 'https://demoblaze.com',
        'qa': 'https://docs.pytest.org'    
    }

    def __init__(self, env) -> None:
        environment = self.get_safe_env(env)
        self.baseurl = self.SUPORTED_URLS[environment]

    def get_safe_env(self, env):
        if env in self.SUPORTED_ENVS:
            return env
        return 'dev'
