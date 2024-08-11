class Section:
    def __init__(self, variables):
        for key, value in variables.items():
            setattr(self, key.lower(), value)

    def __repr__(self):
        return f"{self.__dict__}"

