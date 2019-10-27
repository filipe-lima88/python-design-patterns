class Person(object):
    # constructor
    def __init__(self, name, age):
        # class attributes
        self.name = name  # public attribute
        self.__age = age  # private attribute

    # class method
    def get_person(self):
        return 'Person: {}'.format(self.name)

    def get_age(self):
        return self.__age


p = Person(name='Victor', age=34)
print(p.name)  # works!
# print(p.__age)  # don't work!
print(p.get_age())  # works!
