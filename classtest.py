

class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = []
        print(self.i)

    def f(self):
        self.i = 123
        return 'hello world'


x = MyClass()
print(x.f())




