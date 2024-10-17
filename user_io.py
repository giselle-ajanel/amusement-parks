
# Final Project
# Name: Giselle Ajanel

# Filename: user_io.py
# Description: This file  will define functions that interface with the user.

import helper

# function: displayDict()
# parameter: optionsDict (dictionary with the options and descriptions)
# return value: none
def displayDict(optionsDict):
    keys = list(optionsDict)
    keys.sort()
    for key in keys:
        print(key, "->", optionsDict[key])

# function: getUserOption()
# parameter: optionsDict
# return value: a string that is a valid option entered by the user
def getUserOption(optionsDict):
    options = input("Option: ").strip().upper()
    while options:
        if options in optionsDict:
            return options
        else:
            options = input("Option: ").strip().upper()

# function: displayNumCoasters()
# parameter: coastersList
# return value: none
def displayNumCoasters(coastersList):
    coastersTotal = len(coastersList)
    print("The total number of coasters is", coastersTotal)

# function: displayNumWoodenCoasters()
# parameter: coastersList
# return value: none
def displayNumWoodenCoasters(coastersList):
    count = 0
    for coasters in coastersList:
        if coasters["material_type"] == "Wooden":
            count += 1
    print("The total number of wooden coasters is", count)

# function: displayCoaster()
# parameter: coasterDict
# return value: none
def displayCoaster(coasterDict):
    print(coasterDict["name"] + " " + "[" + coasterDict["park"] + "]")
    if coasterDict["speed"] != "":
        print("\tSpeed =", coasterDict["speed"], "mph")
    if coasterDict["height"] != "":
        print("\tHeight =", coasterDict["height"], "ft")
    if coasterDict["length"] != "":
        print("\tLength =", coasterDict["length"], "ft")
    if coasterDict["num_inversions"] != "" and int(coasterDict["num_inversions"]) > 0:
        print("\tLoops =", coasterDict["num_inversions"])
    print("\tStatus is", coasterDict["status"])

# function: displayLoopiestCoaster()
# parameter: coastersList
# return value: none
def displayLoopiestCoaster(coastersList):
    loopiest = helper.getLoopiestCoaster(coastersList)
    displayCoaster(loopiest)

# function: displayTallestCoaster()
# parameter: coastersList
# return value: none
def displayTallestCoaster(coastersList):
    tallestCoaster = helper.getTallestCoaster(coastersList)
    displayCoaster(tallestCoaster)

# function: makeParksFile()
# parameter: coastersList
# return value: none
# side effect: text file with the names of the unique amusement parks
def makeParksFile(coastersList):
    uniqueNames = helper.getUniqueParkNames(coastersList)
    uniqueNames.sort()
    fileWrite = open("amusement_parks.txt", "w")
    print("Amusement parks in alphabetical order: \n", file=fileWrite)
    for park in uniqueNames:
        print(park, file=fileWrite)
    fileWrite.close()
    print("There are 717 unique parks.")
    print("The park names were saved to amusement_parks.txt")

# function: findCoasters()
# parameter: coastersList
# return value: none
def findCoasters(coastersList):
    searchPhrase = input("Enter a search phrase: ").strip().lower()
    count = 0
    for coaster in coastersList:
        nameCoaster = coaster["name"].lower()
        parkCoaster = coaster["park"].lower()
        if searchPhrase in nameCoaster or searchPhrase in parkCoaster:
            displayCoaster(coaster)
            count += 1
    if count == 0:
        print("No coaster contain " + " '" + searchPhrase + "'")
    else:
        print("Found " + str(count) + " coasters that contain " + "'" + searchPhrase + "'")
