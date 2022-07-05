import random

class PetDataGenerator:

    def getNewPet(self):
        return self.getUpdatePetPyload(random.randint(5, 10000))
    
    def getUpdatePetPyload(self, id):
        return  {
                        "id": id,
                        "category": {
                            "id": 0,
                            "name": "string"
                        },
                        "name": "Pet" + str(random.randint(5, 10000)),
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