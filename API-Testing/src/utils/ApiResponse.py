class ApiResponse():
    def __init__(self, response):
        self.response = response

    def getJson(self):
        return self.response.json()
    
    def assertStatus(self, statusCode):
        errorMessage = "Error status codes not match: expected code:{0}, actual code: {1}".format(statusCode, self.response.status_code)
        assert self.response.status_code == statusCode, errorMessage
        return self