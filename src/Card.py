
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    
    def __str__(self):
        return self.color +':'+ self.value