
class ProductAssertions():
    def equalLists(self, list1, list2):
        """ list are ordered by the first column """
        if len(list1) != len(list2):
            assert False, "Product lists don't have the same lenght"
        
        list1.sort(key=lambda x: x.name)
        list2.sort(key=lambda x: x.name)

        assert list1 == list2, "Product lists are different"

    def priceSumIsEqual(self, list, total):
        listTotal = sum(product.price for product in list)
        assert listTotal == total, "Total price are not equal"
