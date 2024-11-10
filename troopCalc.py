import math
import sys
import os

print("--------------TROOP CALCULATOR-----------------------")
print("TOTAL LEADERSHIP:"+sys.argv[1])
print("-----------------------------------------------------")
leadership = int(sys.argv[1])
dominance = 40000

if "GITHUB_STEP_SUMMARY" in os.environ:
 def print_to_summary(message):
    with open(os.environ['GITHUB_STEP_SUMMARY'],'a') as f:
        f.write(message + '\n')

# the lookup is strength, health, leadership
statLookup = {
    'MELEE-G-9' : (5510,16530,1),
    'FLY-G-9'   : (110200,330600,20),
    'MELEE-G-8' : (3060,9180,1),
    'MELEE-M-9' : (1210000,3630000,55)
}

# This lookup table has kill order from top to bottom
# The values are number of troops, leadership
countLookup = {
    'MELEE-S-8' : [470,1],
    'MOUNT-S-8' : [230,2],
    'RANGE-S-8' : [450,1],
    'FLY-S-8' : [21,20],
    
    'MELEE-S-9' : [225,1],
    'MOUNT-S-9' : [112,2],
    'RANGE-S-9' : [220,1],
    'FLY-S-9' : [10,20],
    
    'MELEE-G-8' : [360,1],
    'MOUNT-G-8' : [175,2],
    'RANGE-G-8' : [345,1],
    'FLY-G-8' : [17,20],

    'MELEE-G-9' : [185,1],
    'MOUNT-G-9' : [90,2],
    'RANGE-G-9' : [175,1],
    'FLY-G-9' : [8,20]
}

battleLookup = {}
battleLookup['S8:S9:G8:G9:MELEE:MOUNT:RANGE:FLY'] = countLookup 

totalVal = 0
for key,value in battleLookup['S8:S9:G8:G9:MELEE:MOUNT:RANGE:FLY'].items():
    totalVal += value[0]*value[1]

percentLookup = {}
for key,value in countLookup.items():
    percentLookup[key] = (value[0]*value[1])/totalVal

finalCountLookup = {}
for key,value in percentLookup.items():
    count = (leadership*value)/countLookup[key][1]
    finalCountLookup[key] = count
    msg = key + ":" + str(round(count)) 
    print(msg)
#    if "GITHUB_STEP_SUMMARY" in os.environ:
#      print_to_summary(msg)

#--------------Print out monster count ------------------
monsterCount = (0.9*statLookup['FLY-G-9'][1]*finalCountLookup['FLY-G-9'])/statLookup['MELEE-M-9'][1]
msg = "Monster M9 count:" + str(math.floor(monsterCount))
print(msg)
#if "GITHUB_STEP_SUMMARY" in os.environ:
#  print_to_summary(msg)
