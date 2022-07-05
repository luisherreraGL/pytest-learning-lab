from test.pet.BasePet import BasePet

class DeletePetTests(BasePet):

    def test_deletePetByID(self, insertedNewPet):
        petId=  str(insertedNewPet['id'])
        expectedResponse = {
                              "code": 200,
                              "type": "unknown",
                              "message": petId
                            }

        response = self.client.delete(self.path + petId).assertStatus(200).getJson()
        assert response == expectedResponse, "Error: actual & expected dictionaries are not equal"
