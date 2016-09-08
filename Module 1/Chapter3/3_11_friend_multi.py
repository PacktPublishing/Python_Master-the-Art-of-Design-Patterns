class Friend(Contact, AddressHolder):
    def __init__(self, name, email, phone,
            street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(
            self, street, city, state, code)
        self.phone = phone
