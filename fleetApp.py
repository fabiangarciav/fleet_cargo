import numpy as np


# Function that return the number of vowels in a string
def countVowels(string):
    num_vowels = 0
    for char in string.lower():
        if char in "aeiouáéíóú":
           num_vowels = num_vowels + 1
    return num_vowels

# Function that return the number of consonants in a string
def countConsonants(string):
    num_Consonants = 0
    for char in string.lower():
        if char in "bcdfghjklmnñopqrstwxyz,.#-_":
           num_Consonants = num_Consonants + 1
    return num_Consonants

# Function that open a text file and return an array with each text line into array
def openTextFiletoArray(fileName,type):
    openFile = open(fileName, 'r', encoding='utf-8')
    array = []
    if type == "driver":
        for textLine in openFile:
            array.append([ textLine, countVowels(textLine), countConsonants(textLine) ])
    elif type == "address":
            for textLine in openFile:
                array.append([ textLine ])
    return array



#textFile = 'C:/Users/Dell Inspiron/OneDrive/Escritorio/address.txt'
#datos = np.genfromtxt(textFile, delimiter=',', dtype='object')


def applySSFactorAlgorithm(arrOfDrivers,arrOfAddress):
    arrIndexBySS = []
    for driver in arrOfDrivers:
        driversName = driver[0]
        for address in arrOfAddress:
            addressName = address[0]
            if len(driversName) == len(addressName):
                boostFactorSS = 1.5
            else:
                boostFactorSS = 1
            if ( len(addressName) % 2) == 0:
                factorSS = driver[1] * boostFactorSS * 1.5 #<-- Multiplay Vowels per Address SS factor
            else:
                factorSS = driver[2] * boostFactorSS * 1 #<-- Multiplay Consonants per Address SS factor
            arrIndexBySS.append([factorSS, driversName, addressName]) #<-- Matrix SS value, Driver's 
    arrIndexBySS = np.array(arrIndexBySS)
    arrIndexBySS = arrIndexBySS[arrIndexBySS[:, 0].argsort()][::-1]
    return arrIndexBySS

arrOfAddress = openTextFiletoArray('C:/Users/Dell Inspiron/OneDrive/Escritorio/address.txt','address')
arrOfDrivers = openTextFiletoArray('C:/Users/Dell Inspiron/OneDrive/Escritorio/drivers.txt','driver')

#arrOfSS = np.array(arrOfSS)
#arrOfSS = arrOfSS[arrOfSS[:, 0].argsort()][::-1]

arrIndexBySS = applySSFactorAlgorithm(arrOfDrivers,arrOfAddress)

bestRoutes = []
isEmptyArray = False
row = 0
while isEmptyArray != True:
    bestRoutes.append(arrIndexBySS[row])
    indexForDelete = np.where( (arrIndexBySS == arrIndexBySS[row,1]) | (arrIndexBySS == arrIndexBySS[row,2]) )[0]
    arrIndexBySS = np.delete(arrIndexBySS, indexForDelete, axis=0)
    if len(arrIndexBySS) == 0:
        isEmptyArray = True

for row in bestRoutes:
    print(row)


