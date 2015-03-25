#Jayshree Sarathy
#jayshree.sarathy@yale.edu
#using Python 3

import sys

#cost of inserting a letter
def insertCost(letter, index):
#penalty for changing first letter
    if (index == 0):
        return 5
    else: return 2

#cost of deleting a letter
def deleteCost(letter, index):
#penalty for changing first letter   
    if (index == 0):
        return 5
    else: return 2

#cost of substituting a letter
def substituteCost(sletter, tletter, tfirst, sindex):
#no cost if the letters are the same
    if (sletter == tletter):
        return 0
#penalty for changing first letter
    elif (sindex == 0):
        return 5
#lower cost if the second letter of the source is first letter of target
    elif (sindex == 1 and sletter == tfirst):
        return 1   
    else:
        return 3
       # return (abs(ord(sletter) - ord(tletter)) * (float(3)/float(255)))

#cost of transposing letters
def transposeCost(sletter, tletter):
#common error is switching e and i
    if (sletter == 'e' and tletter == 'i'):
        return 1
    elif (sletter == 'i' and tletter == 'e'):
        return 1
    else:
        return 2

#decrease cost for common prefix errors
def prefixCost(source, target):
#common error is using un instead of dis at the beginning of a word
    if (source.startswith("un") and target.startswith("dis")):
        return 5
    else: return 0
    
def minEditDistance(target, source):
#lengths of target word and source word
    targetLength = len(target)
    sourceLength = len(source)

#initialize matrix with zeros
    distance = [[0 for x in range(sourceLength + 1)] for y in range(targetLength + 1)]

#initialize target side of array
    for i in range(1, targetLength + 1):
         distance[i][0] = distance[i-1][0] + insertCost(target[i-1], i - 1)
#initialize source side of array
    for j in range(1, sourceLength + 1):
         distance[0][j] = distance[0][j-1] + deleteCost(source[j-1], j - 1)
#go through rest of array and insert mincost
    for k in range(1, targetLength + 1):
         for l in range(1, sourceLength + 1):
             minlist = [distance[k-1][l] + insertCost(target[k-1], k - 1),
                            distance[k-1][l-1] + substituteCost(source[l-1],target[k-1], l-1, target[0]),
                            distance[k][l-1] + deleteCost(source[l-1], l - 1)]
#include transposeCost function if two consecutive letters are switched
             if (1 < k < targetLength and 1 < l < sourceLength
                 and target[k] == source[l-1] and source[l] == target[k-1]):
                minlist.append(distance[k-2][l-2] + transposeCost(source[l], target[k]))
#input the minimum of all different costs into the cell                
             distance[k][l] = min(minlist)
#return the cost in the last cell minus costs for switching common prefixes
    return distance[targetLength][sourceLength] - prefixCost(source, target)

#open and read both files
misspelledwords = open(sys.argv[2]).read().split()
correctwords = open(sys.argv[1]).read().split("\n")

#find the word with the min distance
for word in misspelledwords:
    minlength = minEditDistance(word, correctwords[0])
    correction = correctwords[0]

    for cw in correctwords:
        levDistance = minEditDistance(word, cw)
        if (levDistance <= minlength):
            correction = cw
            minlength = levDistance

#print word with min distance
    print(correction)

