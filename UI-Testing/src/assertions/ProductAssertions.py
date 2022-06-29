
class ProductAssertions():
    def equalLists(self, list1, list2):
        """ list are ordered by the first column """
        if len(list1) != len(list2):
            assert False, "Product lists don't have the same lenght"
        
        list1.sort(key=lambda x: x.name)
        list2.sort(key=lambda x: x.name)

        for item1 in list1:
            print(item1.name)
            print(item1.price)
    
        for item2 in list2:
            print(item2.name)
            print(item2.price)

        assert list1 == list2, "Product lists are different"