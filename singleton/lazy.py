class LazySingleton:
    __instance = None

    def __init__(self):
        if not LazySingleton.__instance:
            print('__init__ method called...')
        else:
            print('Instance already created: {}'.format(self))

    #  @classmethod is used to create a class' method, not an object method. Is similar to static methods.
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance


#  The class is initialized, but don't create a object
s = LazySingleton()
#  The object is created HERE
print('Object created: {}'.format(LazySingleton.getInstance()))
s1 = LazySingleton()
print('Used previously created object: {}'.format(s1))
