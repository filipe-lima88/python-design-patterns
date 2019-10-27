class A:
    def a(self):
        print('method A')


#  Class with composition of itself with 'A'
class B:
    def b(self):
        print('method B')
        A().a()


objB = B()
objB.b()
