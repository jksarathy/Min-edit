#Jayshree Sarathy
#jayshree.sarathy@yale.edu
#using Python 3

import sys

def insertCost(letter):
    return 1;

def deleteCost(letter):
    return 1;

def substituteCost(letter1, letter2):
    if (letter1 == letter2):
        return 0
    else:
        return 2

def minimumCost(a, b, c):
    if (a <= b <= c or a <= c <= b):
        return a
    elif (b <= a <= c or b <= c <= a):
        return b
    else:
        return c
        

def minEditDistance(target, source):
    targetLength = len(target)
    sourceLength = len(source)

    distance = [[0 for x in range(sourceLength + 1)] for y in range(targetLength + 1)]
    
    for i in range(1, targetLength + 1):
         distance[i][0] = distance[i-1][0] + insertCost(target[i-1])
    for j in range(1, sourceLength + 1):
         distance[0][j] = distance[0][j-1] + deleteCost(source[j-1])
    for k in range(1, targetLength + 1):
         for l in range(1, sourceLength + 1):
             distance[k][l] = minimumCost(distance[k-1][l] + insertCost(target[k-1]),
                                               distance[k-1][l-1] + substituteCost(source[l-1], target[k-1]),
                                               distance[k][l-1] + deleteCost(source[l-1]))
    return distance[targetLength][sourceLength]


stringTarget = str( sys.argv[1])
stringSource =str( sys.argv[2])


print(minEditDistance(stringTarget, stringSource))


        
             
         
         
        
    

    
