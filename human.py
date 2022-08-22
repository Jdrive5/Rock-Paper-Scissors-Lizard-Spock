from unicodedata import name
from player import Player

class human(Player):
    
    
    
    def __init__(self, name):
        super().__init__(name)
        self.user_name()