__author__ = 'Chetan'

from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
    
    @abstractmethod
    def execute(self):
        pass

class StockTrade:
    
    def buy(self):
        print("You will buy stocks")
    
    def sell(self):
        print("You will sell stocks")

class Agent:
    
    def __init__(self):
        self.__orderQueue = []
    
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()

class BuyStockOrder(Order):
    
    def __init__(self, stock):
        self.stock = stock
    
    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    
    def __init__(self, stock):
        self.stock = stock
    
    def execute(self):
        self.stock.sell()


if __name__ == '__main__':
    #Client
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)
    
    #Invoker
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)


