__author__ = 'Chetan'

from abc import abstractmethod, ABCMeta

class Trip(metaclass=ABCMeta):
    
    @abstractmethod
    def setTransport(self):
        pass
    
    @abstractmethod
    def day1(self):
        pass
    
    @abstractmethod
    def day2(self):
        pass
    
    @abstractmethod
    def day3(self):
        pass
    
    @abstractmethod
    def returnHome(self):
        pass
    
    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()

class VeniceTrip(Trip):
    
    def setTransport(self):
        print("Take a boat and find your way in the Grand Canal")
    
    def day1(self):
        print("Visit St Mark's Basilica in St Mark's Square")
    
    def day2(self):
        print("Appreciate Doge's Palace")
    
    def day3(self):
        print("Enjoy the food near the Rialto Bridge")
    
    def returnHome(self):
        print("Get souvenirs for friends and get back")


class MaldivesTrip(Trip):
    
    def setTransport(self):
        print("On foot, on any island, Wow!")
    
    def day1(self):
        print("Enjoy the marine life of Banana Reef")
    
    def day2(self):
        print("Go for the water sports and snorkelling")
    
    def day3(self):
        print("Relax on the beach and enjoy the sun")
    
    def returnHome(self):
        print("Dont feel like leaving the beach..")


class TravelAgency:
    
    def arrange_trip(self):
        choice = input("What kind of place you'd like to go historical or to a beach?")
        if choice == 'historical':
            self.venice = VeniceTrip()
            self.venice.itinerary()
        if choice == 'beach':
            self.maldives = MaldivesTrip()
            self.maldives.itinerary()


TravelAgency().arrange_trip()
