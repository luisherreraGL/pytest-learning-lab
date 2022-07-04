from allure import step
from src.assertions.CommonAssertions import CommonAssertions
class ProductAssertions():
    commonAssertions = CommonAssertions()

    @step("Comparing items list cart with added items list")
    def validateitemsCartList(self, list1, list2):
        sortingFunc = lambda x: x.name
        self.commonAssertions.equalLists(list1, list2, sortingFunc)
       
    @step("Comparing total amount against selected items amount")
    def priceSumIsEqual(self, list, total):
        listTotal = sum(product.price for product in list)
        assert listTotal == total, "Amounts are not equal"
