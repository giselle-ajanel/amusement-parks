
# Final Project
# Name: Giselle


# Filename: main_ajanel_giselle.py (update accordingly)
# Description: This file calls functions in helper.py file as well as the user_io.py file.

# import helper file for the main() function
import helper
# import user_io file for the main() function
import user_io

# function: makeOptionsDict()
# parameter: none
# return value: dictionary where keys are letters
def makeOptionsDict():
    dictionaryOptions = {"A" : "Amusement parks", "B" : "Number of coasters",
                         "C" : "Number of wooden coasters", "D" : "Loopiest coaster",
                         "E" : "Tallest coaster", "F" : "Find coasters", "Q": "Quit"}
    return dictionaryOptions

# function: main()
# parameters: none
# return value: none
def main():
    print("Roller Coasters from around the world")
    coasterList = helper.makeCoastersList()
    optionsList = makeOptionsDict()

    user_io.displayDict(optionsList)
    inputUser = user_io.getUserOption(optionsList)
    while inputUser.upper() != "Q":
        if inputUser.upper() == "A":
            user_io.makeParksFile(coasterList)
            print()
            user_io.displayDict(optionsList)
        elif inputUser.upper() == "B":
            user_io.displayNumCoasters(coasterList)
            print()
            user_io.displayDict(optionsList)
        elif inputUser.upper() == "C":
            user_io.displayNumWoodenCoasters(coasterList)
            print()
            user_io.displayDict(optionsList)
        elif inputUser.upper() == "D":
            user_io.displayLoopiestCoaster(coasterList)
            print()
            user_io.displayDict(optionsList)
        elif inputUser.upper() == "E":
            user_io.displayTallestCoaster(coasterList)
            print()
            user_io.displayDict(optionsList)
        elif inputUser.upper() == "F":
            user_io.findCoasters(coasterList)
            print()
            user_io.displayDict(optionsList)
        inputUser = user_io.getUserOption(optionsList)
main()
