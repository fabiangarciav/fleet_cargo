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

arrOfAddress = openTextFiletoArray('C:/Users/Dell Inspiron/OneDrive/Escritorio/address.txt','address')
arrOfDrivers = openTextFiletoArray('C:/Users/Dell Inspiron/OneDrive/Escritorio/drivers.txt','driver')

#textFile = 'C:/Users/Dell Inspiron/OneDrive/Escritorio/address.txt'
#datos = np.genfromtxt(textFile, delimiter=',', dtype='object')

arrOfSS = []
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
        arrOfSS.append([factorSS, driversName, addressName]) #<-- Matrix SS value, Driver's 

arrOfSS = np.array(arrOfSS)
arrOfSS = arrOfSS[arrOfSS[:, 0].argsort()][::-1]

bestRoutes = []
bestDriver = ''
for row in arrOfSS:
    bestRoutes.append(row)
    print(row[1])
    indices = np.where( (arrOfSS == row[1]) | (arrOfSS == row[2]) )[0]
    print(indices)

#Iterating using while loop
#row = 0
#while row < len(arrOfSS):
#    driversName = arrOfSS[row,1]
#    addressName = arrOfSS[row,2]
#    rowToBeAdded = arrOfSS[row,0] + "-" + addressName + "-" + driversName
#    bestRoutes.append(rowToBeAdded)
#    i = 0 
#    while i < len(arrOfSS):
#        if driversName == arrOfSS[i,1]:
 #           print (driversName , "--- ",  arrOfSS[i,1])
#            arrOfSS = np.delete(arrOfSS, i, 0)
#            row = 0
#        elif addressName == arrOfSS[i,2]:
  #          print (addressName , "--- ",  arrOfSS[i,2])
#            arrOfSS = np.delete(arrOfSS, i, 0)
#            row = 0
#        i += 1
#    row += 1
    
#for anyrow in bestRoutes:
#    print (anyrow)
#print(len(bestRoutes))

#print(bestRoutes)
# delete 0 th row

#clearprint(bestRoutes)
#def find_indices(list_to_check, item_to_find):
#    array = np.array(list_to_check)
#    indices = np.where(array == item_to_find)[0]
#    return list(indices)

#print(find_indices(npArrOfSS, npArrOfSS[0,2]))

# Getting length of list
#length = len(npArrOfSS)
#i = 0
   
# Iterating using while loop
#while i < length:
#    print(npArrOfSS[i])
#    i += 1

#print( npArrOfSS[1,1] )
#finded = np.where( arrOfSS == npArrOfSS[0,2] )
#print(finded)
#delete all rows that have less SS of each driver
