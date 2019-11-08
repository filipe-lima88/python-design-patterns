class Monostate:
    __shared_state = {}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


b = Monostate()
b1 = Monostate()
b.x = 4

#  Changing state of a object will change every other's state of same class
print('Object b: {}'.format(b))
print('Object b1: {}'.format(b1))
print('Object state b: {}'.format(b.__dict__))
print('Object state b1: {}'.format(b1.__dict__))

b1.x = 45

print('Object state b: {}'.format(b.__dict__))
print('Object state b1: {}'.format(b1.__dict__))
