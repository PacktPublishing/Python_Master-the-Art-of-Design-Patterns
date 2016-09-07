__author__ = 'Chetan'

from abc import abstractmethod, ABCMeta

class State(metaclass=ABCMeta):
    
    @abstractmethod
    def Handle(self):
        pass

class ConcreteStateB(State):
    def Handle(self):
        print("ConcreteStateB")

class ConcreteStateA(State):
    def Handle(self):
        print("ConcreteStateA")

class Context(State):
    
    def __init__(self):
        self.state = None
    
    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state
    
    def Handle(self):
        self.state.Handle()


context = Context()
stateA = ConcreteStateA()
stateB = ConcreteStateB()

context.setState(stateA)
context.Handle()
