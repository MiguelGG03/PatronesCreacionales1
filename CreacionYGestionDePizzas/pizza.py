class Pizza:
    def __init__(self):
        self._dough = ""
        self._sauce = ""
        self._topping = ""
        self._pairing = ""

    @property
    def dough(self):
        return self._dough
    
    @dough.setter
    def dough(self, dough):
        self._dough = dough

    @property
    def sauce(self):
        return self._sauce
    
    @sauce.setter
    def sauce(self, sauce):
        self._sauce = sauce

    @property
    def topping(self):
        return self._topping
    
    @topping.setter
    def topping(self, topping):
        self._topping = topping
        
    def __str__(self):
        return f"dough: {self.dough}\nsauce: {self.sauce}\ntopping: {self.topping}"