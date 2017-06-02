# Tutaj są funkcje, które są pomocne w rozwiązaniu zadanego problemu, ale nie sę przypisane do żadnej klasy

def CalculateDistanceBurning(Distance, Burning):

    # Obliczenie spalania na Distance kilometrów
    distanceFactor = Distance / 100
    Heuristic = (Burning / Distance) * distanceFactor
    return heuristic