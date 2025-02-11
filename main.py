import os
from functions.input_parser import *
from classes.GraphDesign import Design


path = os.getcwd()
file = path + "/testfile.csv"
os.environ["PATH"] += os.pathsep + r'D:\Users\lorenzoluc\Downloads\windows_10_cmake_Release_Graphviz-12.2.1-win64\Graphviz-12.2.1-win64/bin/'


def app():
    objects = read(file) #read the input file
    elementList = use(objects) #check the entrances and initialize the objects
    allHighways, allPrices = getAllHighways(elementList) #get all coordinates that the highway pass by, with its width


    image = Design()
    g=image.create()
    image.trace(g,elementList) #trace the graph for the objects created

    #The shortest distance between two buildings

    print(f"Calculating the distance between {elementList[0]} and {elementList[2]}")
    elementList[0].distanceTwoBuildings(elementList[2],allHighways,allPrices)

    print(f"Calculating the distance between {elementList[3]} and {elementList[2]}")
    elementList[3].distanceTwoBuildings(elementList[2],allHighways,allPrices)

if __name__ == '__main__':
    app()


