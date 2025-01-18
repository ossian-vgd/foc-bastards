import math
import sys
import os

print("TOTAL LEADERSHIP:"+sys.argv[1])
print("-----------------------------------------------------")
leadership = int(sys.argv[1])
battleplan = sys.argv[2]

def calcResultsv2(leadval, battleplan):

  leadval = int(leadval)
  selectbattleplan = battleplan

  # the lookup is strength, health, leadership
  statLookup = {
    'MELEE-G9' : (5510,16530,1),
    'RANGE-G9' : (5510,16530,1),
    'MOUNT-G9' : (11020,33060,2),
    'FLY-G9'   : (110200,330600,20),
    'MELEE-S9' : (5510,16530,1),
    'RANGE-S9' : (5510,16530,1),
    'MOUNT-S9' : (11020,33060,2),
    'FLY-S9'   : (110200,330600,20),
    'MELEE-G7' : (1700,5100,1),
    'RANGE-G7' : (1700,5100,1),
    'MOUNT-G7' : (3400,10200,2),
    'FLY-G7'   : (34000,102000,20),
    'MELEE-G8' : (3060,9180,1),
    'RANGE-G8' : (3060,9180,1),
    'MOUNT-G8' : (6120,18360,2),
    'FLY-G8'   : (61200,183600,20),
    'MELEE-S8' : (3060,9180,1),
    'RANGE-S8' : (3060,9180,1),
    'MOUNT-S8' : (6120,18360,2),
    'FLY-S8'   : (61200,183600,20),
    'MELEE-M9' : (1210000,3630000,55)
  }

  # BattlePlan (BP1) - S8:S9:G8:G9/Melee:Mount:Range:Fly
  countLookup_BP1 = {
    'MELEE-S8' : [470,1],
    'MOUNT-S8' : [230,2],
    'RANGE-S8' : [450,1],
    'FLY-S8'   : [21,20],

    'MELEE-S9' : [225,1],
    'MOUNT-S9' : [112,2],
    'RANGE-S9' : [220,1],
    'FLY-S9'   : [10,20],
    
    'MELEE-G8' : [360,1],
    'MOUNT-G8' : [175,2],
    'RANGE-G8' : [345,1],
    'FLY-G8'   : [17,20],

    'MELEE-G9' : [185,1],
    'MOUNT-G9' : [90,2],
    'RANGE-G9' : [175,1],
    'FLY-G9'   : [8,20]
  }

  # BattlePlan (BP2) - S8:S9:G8:G9/Melee:Fly:Mount:Range
  countLookup_BP2 = {
    'MELEE-S8' : [470,1],
    'FLY-S8'   : [22,20],
    'MOUNT-S8' : [218,2],
    'RANGE-S8' : [430,1],

    'MELEE-S9' : [230,1],
    'FLY-S9'   : [10,20],
    'MOUNT-S9' : [98,2],
    'RANGE-S9' : [191,1],

    'MELEE-G8' : [342,1],
    'FLY-G8'   : [17,20],
    'MOUNT-G8' : [168,2],
    'RANGE-G8' : [333,1],

    'MELEE-G9' : [180,1],
    'FLY-G9'   : [8,20],
    'MOUNT-G9' : [79,2],
    'RANGE-G9' : [150,1]
  }

  # BattlePlan (BP3) - S8:G8:S9:G9/Melee:Fly:Mount:Range
  countLookup_BP3 = {
    'MELEE-S8' : [470,1],
    'FLY-S8'   : [22,20],
    'MOUNT-S8' : [218,2],
    'RANGE-S8' : [430,1],

    'MELEE-G8' : [420,1],
    'FLY-G8'   : [20,20],
    'MOUNT-G8' : [195,2],
    'RANGE-G8' : [385,1],

    'MELEE-S9' : [212,1],
    'FLY-S9'   : [9,20],
    'MOUNT-S9' : [88,2],
    'RANGE-S9' : [173,1],

    'MELEE-G9' : [170,1],
    'FLY-G9'   : [8,20],
    'MOUNT-G9' : [78,2],
    'RANGE-G9' : [150,1]
  }

  # BattlePlan (BP4) - Skadi G7:G8:G9:S9/Melee:Fly:Mount:Range
  countLookup_BP4 = {
    'MELEE-G7' : [29600,1],
    'FLY-G7'   : [1410,20],
    'MOUNT-G7' : [14250,2],
    'RANGE-G7' : [28388,1],

    'MELEE-G8' : [15680,1],
    'FLY-G8'   : [764,20],
    'MOUNT-G8' : [7590,2],
    'RANGE-G8' : [15080,1],
    
    'MELEE-G9' : [6930,1],
    'FLY-G9'   : [327,20],
    'MOUNT-G9' : [3220,2],
    'RANGE-G9' : [6340,1],

    'MELEE-S9' : [9170,1],
    'FLY-S9'   : [424,20],
    'MOUNT-S9' : [4190,2],
    'RANGE-S9' : [8280,1]

  }
  
  battleLookup = {}
  battleLookup['S8:S9:G8:G9:MELEE:MOUNT:RANGE:FLY'] = countLookup_BP1
  battleLookup['S8:S9:G8:G9:MELEE:FLY:MOUNT:RANGE'] = countLookup_BP2
  battleLookup['S8:G8:S9:G9:MELEE:FLY:MOUNT:RANGE'] = countLookup_BP3 
  battleLookup['SKADI:G7:G8:G9:S9:MELEE:FLY:MOUNT:RANGE'] = countLookup_BP4

  totalVal = 0
  for key,value in battleLookup[selectbattleplan].items():
#    print("DA VALUE:"+key+":"+str(value[0])+":"+str(value[1]))
    totalVal += value[0]*value[1]

  percentLookup = {}
  for key,value in battleLookup[selectbattleplan].items():
    percentLookup[key] = (value[0]*value[1])/totalVal
#    print("Percent:"+key+":"+str(percentLookup[key]))

  finalCountLookup = {}
  maxTroopHealth = 0
  minTroopHealth = 100000000000
  msg = "<table border=\"1\" style=\"width:25%\"><tr><th align=\"left\">Troop Type</th><th align=\"left\">Count</th></tr>"
  for key,value in percentLookup.items():
    count = (leadval*value)/battleLookup[selectbattleplan][key][1]
    finalCountLookup[key] = count
    maxTroopHealth = max(count*statLookup[key][1],maxTroopHealth)
    minTroopHealth = min(count*statLookup[key][1],minTroopHealth)
#    print("Leadval:"+str(leadval)+"value:"+str(value)+"count:"+str(battleLookup[selectbattleplan][key][1])+"finalcount:"+str(count))
    msg += "<tr><td>"+key + "</td><td>" + str(round(count)) + "</td></tr>"

  #--------------Print out monster count ------------------
  monsterCount = (0.9*minTroopHealth)/statLookup['MELEE-M9'][1]
  msg += "<tr><td>M9 - Follow Guards</td><td>" + str(math.floor(monsterCount)) + "</td></tr>"
  monsterCount = (1.1*maxTroopHealth)/statLookup['MELEE-M9'][1]
  msg += "<tr><td>M9 - Ahead of Guards</td><td>" + str(math.floor(monsterCount)) + "</td></tr></table>"

  return msg

retVal = calcResultsv2(leadership,battleplan)
print(retVal)
