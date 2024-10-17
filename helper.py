# ITP 115, Spring 2023
# Final Project
# Name: Giselle Ajanel
# Email: ajanel@usc.edu
# Section: TacoCat
# Filename: helper.py
# Description: This file will define functions that will be called from other Python files.

# function: makeCoastersList()
# parameter: filenameStr (the name of the CSV file)
# return value: a list of dictionaries where each dictionary represents one roller coaster
def makeCoastersList(filenameStr="roller_coasters.csv"):
    # create a list to hold a list of coasters
    coasterList = []
    # open the file for reading, which creates a file variable
    coasterFile = open(filenameStr, "r")
    # read the keys in the first line
    headerRow = coasterFile.readline()
    headerRow = headerRow.strip("\n")
    rollerList = headerRow.split(",")
    # loop through the rest of the keys
    for line in coasterFile:
        line = line.strip()
        line = line.split(",")
        coaster = {}
        for dictionLine in range(len(rollerList)):
            coaster[rollerList[dictionLine]] = line[dictionLine]
        coasterList.append(coaster)
    # close the file
    coasterFile.close()
    # return the list
    return coasterList

# function: getUniqueParkNames()
# parameter: coastersList (list of dictionaries - each dictionary represents a roller coaster)
# return value: a list of strings where each string is the name of a park
def getUniqueParkNames(coastersList):
    # create variable to hold list of park names
    parkNames = []
    for coaster in coastersList:
        namePark = coaster["park"]
        if namePark not in parkNames:
            parkNames += [namePark]
    parkNames.sort()
    return parkNames

# function: getLoopiestCoaster()
# parameter: coastersList
# return value: dictionary containing one coaster (largest value for number of loops)
def getLoopiestCoaster(coastersList):
    mostLoops = 0
    loopiest = {}
    for coaster in coastersList:
        inversions = coaster["num_inversions"]
        if inversions.isdigit():
            num_inversions = int(inversions)
            if num_inversions > mostLoops:
                mostLoops = num_inversions
                loopiest = coaster
    return loopiest

# function: getTallestCoaster()
# parameter: coastersList
# return value: dictionary with one coaster (largest value for height)
def getTallestCoaster(coastersList):
    heightMax = 0
    tallestCoaster = {}
    for coaster in coastersList:
        heightString = coaster["height"]
        if heightString.isdigit():
            height = int(heightString)
            if height > heightMax:
                heightMax = height
                tallestCoaster = coaster
    return tallestCoaster






