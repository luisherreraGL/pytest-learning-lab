from src.dataGenerators.PetDataGenerator import PetDataGenerator
from test.pet.BasePet import BasePet
class PostPetTests(BasePet):

    def test_addPet(self):
        payloadJson = PetDataGenerator().getNewPet()
        
        response = self.client.post(self.path, payloadJson).assertStatus(200).getJson()
        assert response == payloadJson, "Error: actual & expected dictionaries are not equal"
