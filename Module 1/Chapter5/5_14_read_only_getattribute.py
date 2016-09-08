class ReadOnlyY:
    def __getattribute__(self, attr):
        if attr == "y":
            return "Just Try and Change Me!"
        return super().__getattribute__(attr)
