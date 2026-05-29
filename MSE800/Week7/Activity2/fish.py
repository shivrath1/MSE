from abc import ABC, abstractmethod

class Fish(ABC):

    @abstractmethod
    def category(self):
        pass


class Goldfish(Fish):

    def category(self):
        return "Freshwater"


class Shark(Fish):

    def category(self):
        return "Predator"


class Angelfish(Fish):

    def category(self):
        return "Tropical"


class Tuna(Fish):

    def category(self):
        return "Saltwater"


class Salmon(Fish):

    def category(self):
        return "Migratory"