from math import sqrt, pow, fabs

class Town(): 
    def __init__(self, title, myX, myY):
        self.title = title
        self.X = myX
        self.Y = myY

    def CalculateTownsDistance(self, TownB):
        
        # Obliczenie odległości między dwoma punktami 
        distance = fabs(sqrt(pow((TownB.X - self.X), 2) + pow((TownB.Y - self.Y), 2)))
        return distance