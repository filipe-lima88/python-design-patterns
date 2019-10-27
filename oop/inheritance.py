#  Parent class
class A:
    def a(self):
        print('a')


#  Class with inheritance
class B(A):
    def b(self):
        print('b')


#  Object 'b' can access the methods of its parent.
b = B()
b.a()
