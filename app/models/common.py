class Entity:
    def __init__(self, data = {}):
        for key in data.keys():
            self.__dict__[key] = data[key]