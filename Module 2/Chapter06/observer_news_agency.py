__author__ = 'Chetan'

class NewsPublisher:
    
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None
    
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)
    
    def detach(self):
        return self.__subscribers.pop()
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()
    
    def addNews(self, news):
        self.__latestNews = news
    
    def getNews(self):
        return "Got News:", self.__latestNews


from abc import ABCMeta, abstractmethod

class Subscriber(metaclass=ABCMeta):
    
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber:
    
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class EmailSubscriber:
    
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class AnyOtherSubscriber:
    
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
        print("\nSubscribers:", news_publisher.subscribers())
        
        news_publisher.addNews('Hello World!')
        news_publisher.notifySubscribers()
        
        print("\nDetached:", type(news_publisher.detach()).__name__)
        print("\nSubscribers:", news_publisher.subscribers())
        
        news_publisher.addNews('My second news!')
        news_publisher.notifySubscribers()
