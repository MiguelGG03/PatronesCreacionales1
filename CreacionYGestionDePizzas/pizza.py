class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.topping = ""

    def __str__(self):
        return f"dough: {self.dough}\nsauce: {self.sauce}\ntopping: {self.topping}"