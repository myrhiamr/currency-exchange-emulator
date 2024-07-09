class Currency:
    
    currencies =  {'CHF': 0.930023, # swiss franc
                   'CAD': 1.264553, # canadian dollar
                   'GBP': 0.737414, # british pound
                   'JPY': 111.019919, # japanese yen
                   'EUR': 0.862361, # euro
                   'USD': 1.0} # us dollar
    
    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        """
        An Currency object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    def __repr__(self):
        return f"{self.value:.2f} {self.unit}"
    
    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        if isinstance(other, Currency):
            if other.unit != self.unit:
                other.changeTo(self.unit)
            return Currency(self.value + other.value, self.unit)
        elif isinstance(other, (int, float)):
            return Currency(self.value + (other / Currency.currencies[self.unit]), self.unit)
        else:
            raise TypeError("Unsupported type for addition")
    
    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, Currency):
            if other.unit != self.unit:
                other.changeTo(self.unit)
            return Currency(self.value - other.value, self.unit)
        elif isinstance(other, (int, float)):
            return Currency(self.value - (other / Currency.currencies[self.unit]), self.unit)
        else:
            raise TypeError("Unsupported type for subtraction")
    
    def __isub__(self, other):
        return self.__sub__(other)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Currency((other / Currency.currencies[self.unit]) - self.value, self.unit)
        else:
            raise TypeError("Unsupported type for subtraction")

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3)
print(3 + v1)
print(v1 - 3)
print(30 - v2)
