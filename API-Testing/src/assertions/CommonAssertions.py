class CommonAssertions():
    def compareDictionaries(self, expectedDict, actualDict):
        assert expectedDict == actualDict, "Error: dictionaries not match expected: {0}, actual: {1}".format(expectedDict, actualDict)