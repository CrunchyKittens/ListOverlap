'''
Created on Jan 27, 2018

@author: Mike
'''
# Take two lists:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.
import random
print 'PART A'
print "Returns the values common to two pre-defined lists of different length"
print ""

# 1. create 2 lists make sure they are different lengths
listA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


print "List 1:"
print listA
print ""

print "List 2:"
print listB
print ""


# 2. create 1 empty list
listC = []

# 3. find out which list is longer then loop through the longer list and compare contents of shorter list.
# then append items that appear on both list to listC

if (listA > listB):
    for i in listA:
        if (i in listB):
            listC.append(i)
else:
    for i in listB:
        if (i in listA):
            listC.append(i)

#4. print listC
print "These items are in both lists"
print listC
print ""
    
# Extras:

# Randomly generate two lists to test this
print "PART B"
print "The lists will now be generated randomly"
print ""    

# create two list with randomly generated lengths. Lists must be different lengths
lengthList1 = 0
lengthList2 = 0
while (lengthList1 == lengthList2):
    lengthList1 = random.randint(1,30)
    lengthList2 = random.randint(1,30)

# fill lists with randomly generated numbers between 1-100
listA = []
for i in range(lengthList1):
    listA.append(random.randint(1,100))
print "List 1:"
print listA
print ""
    
listB = []
for i in range(lengthList2):
    listB.append(random.randint(1,100))
print "List 2:"
print listB
print ""

# find out which list is longer then loop through the longer list and compare contents of shorter list.
# then append items that appear on both list to listC
listC = []
if (listA > listB):
    for i in listA:
        if (i in listB):
            listC.append(i)
else:
    for i in listB:
        if (i in listA):
            listC.append(i)

#4. print listC
print "These items are in both lists"
print listC






    


        
