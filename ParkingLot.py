#Title - Calculating optimum size of a parking lot
#Author - Rakin Chowdhury
#Owners - Rakin Chowdhury, Florence Townend, James Senior, Freiya Ketteridge
#Date - 07/02/19


# numpy and pandas pakages require external instaltion
import numpy as np
import math
import pandas as pd

# BlockingProb(phi, c) - Function to return blocking probailty for a M/G/c/c Queue,
# Takes phi = (lamda(rate) / mu (1/mean)) as [int or float] and c (available parking spots) as [int only]
# Returns Bc (Blocking probailty for given phi and mu) as [float]
def BlockingProb(phi, c):
    # This function will use an itterative numercial method to caluate the Blocking probablity
    # starting from c = 0 (no parking spaces) to c = c (c parking spaces)

    # initial value, at c = 0, B = 1 as there is no avliabvle spaces
    Bn = 1

    #itterate formula from c = 0 to c = c. This will return Bc (blocking ratio at c)
    for cn in range(c):
        Bn = (phi * Bn) / ((cn+1) + phi * Bn)

    return Bn

# VarryC(phi, cArray) = Function to calcuate the blokcing prob for different values of c,
#takes phi as [float or int] and as cArray [Array[int]]
# returns table (table of results) as [Pandas.DataFrame]
def VarryC(phi, cArray):
    results = [] # Array to store results

    #itterate over all values of c and append result to the array "results"
    for cn in cArray:
        B =  BlockingProb(phi, cn)
        results.append([cn, B])

    #Adding data to pandas data frame for ease of comparison
    table = pd.DataFrame(results,  columns = ['Parking Spaces', 'Blocking Probailty'])
    return table

#Function to caluate the minum number of parking spaces need with a given phiself
#Takes phi  as [int or Float], c0 (initial c (number of parking spots)) as [int only] and blockingThershold (probablity) as [Float]
#Returns c (minimum parking spots within threshold) [int], bn (Bloacking Probailty) [Float]
def MinimumBn(phi, c0, blockingThershold):

    bn = 1
    while bn > blockingThershold:
        c0 = c0 + 1
        bn = BlockingProb(phi, c0)

    return[c0, bn]



#print("For lamda = 60, and mean = 2.5 and  and varrying parking spaces [150, 155, 160]")
#print(VarryC(150, [150,155,160]))
#print(MinimumBn(150, 50, 0.05))
