from unittest.mock import Base
from test.pet.BasePet import BasePet
from src.dataGenerators.PetDataGenerator import PetDataGenerator

class UpdatePetTests(BasePet):

    def test_updatePetName(self):
        payload = PetDataGenerator().getUpdatePetPyload(401)

        response = self.client.put(self.path, data=payload).assertStatus(200).getJson()
        self.commonAssertions.compareDictionaries(payload, response)