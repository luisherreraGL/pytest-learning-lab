from allure import step
import re

class CommonAssertions():
    @step("Validate {3} matches")
    def assertEqualString(self, string1, string2, field):
        errorMessage = "Error: {0} not matches: expected {1} actual {2}".format(field, string1, string2)
        assert string1 == string2, errorMessage

    @step("Validate {3} value")
    def assertEqualToRegex(self,regexpression, value, field):
       """preppend r to regexpression"""
       errorMessage = "Error: {0} not comply regex expression: {1} value {2}".format(field, regexpression, value)
       pat = re.compile(regexpression)
       assert re.fullmatch(pat, value), errorMessage

    def equalLists(self, list1, list2, sortingFunc = None):
        """ list are ordered by the first column or sortingFunc """
        if len(list1) != len(list2):
            assert False, "Lists don't have the same lenght"

        if sortingFunc: 
            list1.sort(key=sortingFunc)
            list2.sort(key=sortingFunc)

        assert list1 == list2, "Lists are different"