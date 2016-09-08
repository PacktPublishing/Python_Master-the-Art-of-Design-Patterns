class Agent:
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
        }

    def __init__(self):
        self.property_list = []

    def display_properties():
        for property in self.property_list:
            property.display()
