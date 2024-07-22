class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.inner_list = self.list_of_list.pop(0)
        return self

    def get_inner_list(self):
        if len(self.list_of_list) != 0:
            self.inner_list = self.list_of_list.pop(0)
        else:
            raise StopIteration
        return self

    def __next__(self):
        for value in self.inner_list:
            self.value = value
            print(self.value)
        self.get_inner_list()

        return self.value

if __name__ == '__main__':
    l = [[1, 2, 3, 4], [5, 6, 7], [8,'ddf',10],['ddffkkk', 34]]
    print(list(FlatIterator(l)))
