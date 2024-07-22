class IteratorTemplate:
    def __init__(self):
        pass

    def __iter__(self):
        print('enter')
        return self

    def __next__(self):
        print('iteration')
        return 'item'


iterator = IteratorTemplate()
for item in iterator:
    print(item)
