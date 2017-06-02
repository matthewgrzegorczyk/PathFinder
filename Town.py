class Town():
    def __init__(self, myX, myY):
        self.X = myX
        self.Y = myY

    def CalculateTownsDistance(self, TownB):
        from math import sqrt, pow, fabs
 
        # Obliczenie odległości między dwoma punktami 
        distance = fabs(sqrt(pow((TownB.X - self.X), 2) + pow((TownB.Y - self.Y), 2)))
        return distance

    def CalculateHeuristicDistance(self, TownB, Distance):
        return NotImplemented