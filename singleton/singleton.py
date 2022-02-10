
class SingletonError(Exception):
    pass

class Singleton:

    singleton = None

    def __init__(self):
        try: 
            if Singleton.singleton is not None:
                raise SingletonError
        except SingletonError:
            print("There can only be one object of this type")

    @classmethod
    def get_instance(cls):
        if cls.singleton is None:
            cls.singleton = cls()
        print(cls.singleton)
        return cls.singleton

singleton = Singleton.get_instance()
singleton = Singleton.get_instance()
singleton2 = Singleton()
