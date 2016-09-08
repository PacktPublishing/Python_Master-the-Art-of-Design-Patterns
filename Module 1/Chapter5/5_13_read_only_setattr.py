class ReadOnlyX:
    def __setattr__(self, attr, value):
        if attr == "x":
            raise AttributeError("X is immutable")
        super().__setattr__(attr, value)
