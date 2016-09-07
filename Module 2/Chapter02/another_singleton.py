__author__ = 'Chetan'

class Singleton(object):
    cls_attr = None
    def __new__(cls, *args, **kwargs):
        if Singleton.cls_attr:
            raise Exception
        Singleton.cls_attr = 1
        return super(Singleton, cls).__new__(cls, *args, **kwargs)

s = Singleton()
print("Object created", s) ## Object got created
s1 = Singleton() ## Exception thrown
