import requests
import random
from src.utils.RestApiClient import RestApiClient

class PostPetTests():
    client = RestApiClient('https://petstore.swagger.io/')
    path = 'v2/pet'

    def test_addPet(self):
        payloadJson =  {
                        "id": random.randint(5, 10000),
                        "category": {
                            "id": 0,
                            "name": "string"
                        },
                        "name": "windog",
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

        r = self.client.post(self.path, payloadJson).assertStatus(200).getJson()

     
        assert r == payloadJson, "Error: actual & expected dictionaries are not equal"

   