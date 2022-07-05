import requests
from src.utils.RestApiClient import RestApiClient

class GetPetTests():
    client = RestApiClient('https://petstore.swagger.io/')
    path = 'v2/pet/'

    def test_petNotFound(self):
        expectedJson = {'code': 1, 'type': 'error', 'message': 'Pet not found'}

        r = self.client.get(self.path + '30').assertStatus(404).getJson()
     
        assert r == expectedJson, "Error: actual & expected dictionaries are not equal"

    def test_petFound(self):
        expectedJson = {
                            "id": 1,
                            "category": {
                                "id": 0,
                                "name": "string"
                            },
                            "name": "doggie",
                            "photoUrls": [
                                "string"
                            ],
                            "tags": [
                                {
                                    "id": 0,
                                    "name": "string"
                                }
                            ],
                            "status": "available"
                        }

        r = self.client.get(self.path + '1').assertStatus(200).getJson()
     
        assert r == expectedJson, "Error: actual & expected dictionaries are not equal"