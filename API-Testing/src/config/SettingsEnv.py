import os

class SettingsEnv:
    SUPORTED_ENVS = ('qa', 'dev')
    envConfig = {
        'dev': {
            'baseurl': 'https://petstore.swagger.io/'
        },
        'qa': {  
            'baseurl': 'https://petstoreddd.swagger.io/' 
        }
    }

    def getEnvConfig(self):
        environment = self.getSafeEnv(os.getenv('ENV'))
        return self.envConfig[environment]

    def getSafeEnv(self, env):
        if env in self.SUPORTED_ENVS:
            return env
        return 'dev'
