# Simple version, using composition, of something that is very
# complicated using multiple inheritance (as in the book)

from abc import ABC, abstractmethod, abstractproperty

class Property(ABC):
    pass

class House(Property):
    def __init__(self, square_ft: int, balcony: bool):
        self.square_ft = square_ft
        self.balcony = balcony
    
    def __str__(self):
        text = "HOUSE DATA\n"
        text += f"Surface: {self.square_ft}\n"
        text += f"Balcony: {self.balcony}\n"
        return text

class ContractType(ABC):
    pass

class Rental(ContractType):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        text = "RENTAL DATA\n"
        text += f"Rental value: {self.value}\n"
        return text

class Contract:
    def __init__(self, property: Property, type: ContractType):
        self.property = property
        self.type = type
    
    def __str__(self):
        text = f"{self.property} \n"
        text += f"{self.type}"
        return text

house = House(70, True)
rental = Rental(100)
contract = Contract(house, rental)
print(contract)