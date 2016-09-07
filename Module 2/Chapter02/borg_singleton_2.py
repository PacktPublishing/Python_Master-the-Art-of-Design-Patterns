__author__ = 'Chetan'

class Borg(object):
     _shared_state = {}
     def __new__(cls, *args, **kwargs):
       obj = super(Borg, cls).__new__(cls, *args, **kwargs)
       obj.__dict__ = cls._shared_state
       return obj
