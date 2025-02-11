import pandas as pd
from classes.GraphObjects import *
from functions.conditions import *


def read(file):
    return pd.read_csv(file, sep=';')

def use(df):
    elementDic = {}

    IntegerHighway(df) #check if the values are integer or tuple of integer

    contiguous(df) #check if the buildings with the same id are contiguos

    #reading the df and initialize the objects
    for index, row in df.iterrows():
        id_value = row["id"]
        x_value = row["x"]
        x_value = is_valid_integer(x_value)[1]
        y_value = row["y"]
        y_value = is_valid_integer(y_value)[1]
        width_value = row["width"]

        if id_value not in elementDic:
            elementDic[id_value] = [[x_value,y_value,width_value]]
        else:
            elementDic[id_value].append([x_value,y_value,width_value])

    creation = GraphFactory.create_element(elementDic)

    return(creation) #ex: [warehouse1,building1,highway1,highway2...]

def getAllHighways(ObjList):
    allHighways = []
    allPrices = []

    for x in ObjList:
        if x.typology == "highway":
            h,p = x.pathstops()
            allHighways.extend(h)
            allPrices.extend(p)

    return allHighways,allPrices #ex: [(92,100),(93,100),(93,100),(94,100)] and [1,1,2,2]