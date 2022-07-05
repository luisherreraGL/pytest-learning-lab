import requests
import json
from src.utils.ApiResponse import ApiResponse

class RestApiClient():
    def __init__(self, baseURL):
        self.baseURL = baseURL

    def get(self, path, parameters = None, header = None):
        r = requests.get(url = self.buildURL(path), params=parameters, headers=self.buildHeaders(header))
        return ApiResponse(r)

    def buildURL(self, path):
        return self.baseURL + path

    def buildHeaders(self, headers):
        defaultHeaders = {'Content-Type': 'application/json'}
        if headers:
            defaultHeaders.update(headers)

        return defaultHeaders


    def post(self, path, data, parameters = None, header = None):
        r = requests.post(url = self.buildURL(path), data = json.dumps(data), params=parameters, headers=self.buildHeaders(header))
        return ApiResponse(r)