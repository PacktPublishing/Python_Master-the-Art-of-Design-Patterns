    def __enter__(self):
        self.load()
        return self

    def __exit__(self, type, value, tb):
        self.save()
