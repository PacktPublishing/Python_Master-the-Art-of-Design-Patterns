class Color:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name

    def set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name
    
    def get_name(self):
        return self._name
