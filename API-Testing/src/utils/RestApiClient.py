import requests
from src.utils.ApiResponse import ApiResponse 

class RestApiClient():
    def __init__(self, baseURL):
        self.baseURL = baseURL

    def get(self, path, parameters = None, header = None):
        r = requests.get(url = self.buildURL(path), params=parameters, headers= header)
        return ApiResponse(r)

    def buildURL(self, path):
        return self.baseURL + path