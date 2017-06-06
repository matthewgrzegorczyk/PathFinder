# Tutaj są funkcje, które są pomocne w rozwiązaniu zadanego problemu, ale nie sę przypisane do żadnej klasy
from math import acos, cos, sin, fabs, sqrt, pi
import json


def CalculateDistanceBurning(Distance, Burning):

    # Obliczenie spalania na Distance kilometrów
    distanceFactor = Distance / 100
    Heuristic = (Burning / Distance) * distanceFactor
    return heuristic


def calculate_distance(pA, pB):
    """
    # useful links
    # https://pl.wikibooks.org/wiki/Astronomiczne_podstawy_geografii/Odleg%C5%82o%C5%9Bci
    # http://www.latlong.net/
        
    WORK IN PROGRESSSSSSSSSS
      
    """

    # maxLat = 90
    # degreeToMeteres = 111100
    #
    # print(pA)
    # print(pB)
    # dLatA = maxLat - pA[0]
    # dLatB = maxLat - pB[0]
    #
    # print(dLatA)
    # print(dLatB)
    #
    #
    # distance = 0
    #
    # partial = cos(dLatA) * cos(dLatB) + sin(dLatA) * sin(dLatB) * cos(pA[1]-pB[1])
    # print(partial)
    # l = acos(partial)
    # print(l)
    # distance = l * degreeToMeteres

    # Obliczanie odległości w linii prostej pomiędzy dwoma punktami na mapie pomijając krzywiznę Ziemi.
    # Zwracana wartość jest w kilometrach.
    distance = (pA[0] - pB[0])**2
    distance += (cos((pA[0] * pi)/180) * (pB[1] - pA[1]))**2
    distance = sqrt(distance) * (40075.704/360)
    return distance

def import_data(filename):
    h_file = open(filename, 'r')
    cities = {}
    for line in h_file:
        fields = line.split(',')
        name = fields[0].strip()
        lat = float(fields[1])
        lng = float(fields[2])
        cities[name] = (lat, lng)

    return cities
