class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)
