class Singleton:
    def __new__(cls, *args, **kwargs):
        #  If 'instance' attribute does not exist, create it with '__new__' method of super class (Object, in this case)
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


#  The 2 objects 's' and 's2' will be the same instance
s = Singleton()
print(s)

s2 = Singleton()
print(s2)
