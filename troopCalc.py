import math
import sys
import os

print("TOTAL LEADERSHIP:"+sys.argv[1])
print("-----------------------------------------------------")
leadership = int(sys.argv[1])
dominance = 40000

def calcResults(leadval):
  
  leadval = int(leadval)

  # the lookup is strength, health, leadership
  statLookup = {
    'MELEE-G9' : (5510,16530,1),
    'FLY-G9'   : (110200,330600,20),
    'MELEE-G8' : (3060,9180,1),
    'MELEE-M9' : (1210000,3630000,55)
  }

  # This lookup table has kill order from top to bottom
  # The values are number of troops, leadership
  countLookup = {
    'MELEE-S8' : [470,1],
    'MOUNT-S8' : [230,2],
    'RANGE-S8' : [450,1],
    'FLY-S8' : [21,20],
    
    'MELEE-S9' : [225,1],
    'MOUNT-S9' : [112,2],
    'RANGE-S9' : [220,1],
    'FLY-S9' : [10,20],
    
    'MELEE-G8' : [360,1],
    'MOUNT-G8' : [175,2],
    'RANGE-G8' : [345,1],
    'FLY-G8' : [17,20],

    'MELEE-G9' : [185,1],
    'MOUNT-G9' : [90,2],
    'RANGE-G9' : [175,1],
    'FLY-G9' : [8,20]
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
  msg = "<table border=\"1\" style=\"width:25%\"><tr><th align=\"left\">Troop Type</th><th align=\"left\">Count</th></tr>"
  for key,value in percentLookup.items():
    count = (leadval*value)/countLookup[key][1]
    finalCountLookup[key] = count
    msg += "<tr><td>"+key + "</td><td>" + str(round(count)) + "</td></tr>" 

  #--------------Print out monster count ------------------
  monsterCount = (0.9*statLookup['FLY-G9'][1]*finalCountLookup['FLY-G9'])/statLookup['MELEE-M9'][1]
  msg += "<tr><td>M9</td><td>" + str(math.floor(monsterCount)) + "</td></tr></table>"
  return msg 

retVal = calcResults(leadership)
print(retVal)
