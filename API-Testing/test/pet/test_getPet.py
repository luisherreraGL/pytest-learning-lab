from test.pet.BasePet import BasePet
class GetPetTests(BasePet):

    def test_petNotFound(self):
        expectedJson = {'code': 1, 'type': 'error', 'message': 'Pet not found'}

        response = self.client.get(self.path + '4789372').assertStatus(404).getJson()
        assert response == expectedJson, "Error: actual & expected dictionaries are not equal"

    def test_petFound(self, insertedNewPet):
        expectedJson =  insertedNewPet

        response = self.client.get(self.path + str(expectedJson['id'])).assertStatus(200).getJson()
        self.commonAssertions.compareDictionaries(expectedJson, response)