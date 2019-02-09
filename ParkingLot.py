#Title - Calculating optimum size of a parking lot
#Author - Rakin Chowdhury
#Owners - Rakin Chowdhury, Florence Townend, James Senior, Freiya Ketteridge
#Date - 07/02/19


# numpy and pandas pakages require external instaltion
import numpy as np
import math
import pandas as pd
import sys
import matplotlib.pyplot as plt

# BlockingProb(phi, c) - Function to return blocking probailty for a M/G/c/c Queue,
# Takes phi = (lamda / mu ) as [int or float] and c (available parking spots) as [int only]
# Returns Bc (Blocking probailty for given phi and mu) as [float]
def BlockingProb(phi, c):
    # This function will use an itterative numercial method to caluate the Blocking probablity
    # starting from cn = 0 (no parking spaces) to cn = c (c parking spaces)

    # initial value, at c = 0, B = 1 as there is no avliabvle spaces
    Bn = 1

    #itterate formula from cn = 0 to cn = c. This will return Bc (blocking ratio at c)
    for cn in range(c):
        Bn = (phi * Bn) / ((cn+1) + phi * Bn)

    return Bn


#Used for testing
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
#Takes phi  as [int or Float] and blockingThershold (probablity) as [Float]
#Returns c (minimum parking spots within threshold) [int], bn (Bloacking Probailty) [Float]
def MinimumBn(phi,blockingThershold):
    bn = 1
    cn = 1
    while bn > blockingThershold:
        cn = cn + 1
        bn = BlockingProb(phi, cn)


    return[cn, bn]

# Function to Visually show how the optimum value is optained
#Takes phi  as [int or Float] and blockingThershold (probablity) as [Float]
#Returns pyplot graph
def MinBnVisual(phi, threshold):
    #Same processes as MinimumBn, which addition of arrays to record data.
    bn = 1
    cn = 1
    bArray = []
    cArray = []
    FoundOptimum = False
    while bn > 0.0000001:
        cn = cn + 1
        bn = BlockingProb(phi, cn)
        cArray.append(cn)
        bArray.append(bn)
        if FoundOptimum == True:
            b = bn
            c = cn
            FoundOptimum = False
        if bn > threshold:
            FoundOptimum = True



    # Plotting data
    plt.axhline(y = threshold, linestyle='--', color = 'g')
    plt.plot(cArray, bArray, 'r')
    plt.plot([c],[b], 'o')
    plt.annotate(f"({c} , {round(b,4)} )", (c,b), xytext=(c, b + 0.1), arrowprops=dict(arrowstyle="->"), fontsize = 11)
    plt.xlabel('Parking Spaces (c)', fontsize = 16)
    plt.ylabel('Blocking Probailty (b)', fontsize = 16)
    plt.legend(["Minimum Blocking probablity","Blocking Probailty as C increases", "Optimum Value"], fontsize = 11)
    plt.title("Calculating The Minimum Required Parking Spaces", fontsize = 16)

    plt.show()

    return

# help Function
def help():
    print("""
    Help:

    Ussage:
    - MinBn [Phi] [Minimum Bn]
        "Returns Maxmium c for Minimum Bn"
    - VisBn [Phi] [Minimum Bn]
        "Plots Bn agaisnt Cn"

    Key:
    - Lamba = Rate
    - mu = 1 / Mean
    - Phi = Lamba / mu
    - Bn = Blocking Probailty
    - c = Parking Spaces

            """)


#Main
if __name__=='__main__':

    if len(sys.argv) != 4:
        help()
    elif sys.argv[1] == "MinBn":
        print(MinimumBn(float(sys.argv[2]), float(sys.argv[3])))
    elif sys.argv[1] == "VisBn":
        MinBnVisual(float(sys.argv[2]), float(sys.argv[3]))

    else:
        print("Incorrect Ussage")
        help()
