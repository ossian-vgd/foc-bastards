print("--------------TROOP CALCULATOR-----------------------")

leadership = 248000
dominance = 40000

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

totalVal = 0
for key,value in countLookup.items():
    totalVal += value[0]*value[1]

percentLookup = {}
for key,value in countLookup.items():
    percentLookup[key] = (value[0]*value[1])/totalVal


kill_1 = 'MELEE'
kill_2 = 'FLY'
kill_3 = 'MOUNT'
kill_4 = 'RANGE'

finalCountLookup = {}
for key,value in percentLookup.items():
    count = (leadership*value)/countLookup[key][1]
    finalCountLookup[key] = count 
    print(key + ":" + str(round(count)))

#--------------Print out monster count ------------------
flierhealth = statLookup['FLY-G-9'][1]
fliercount = finalCountLookup['FLY-G-9']
monsterhealth = statLookup['MELEE-M-9'][1]
monsterCount = (statLookup['FLY-G-9'][1]*finalCountLookup['FLY-G-9'])/statLookup['MELEE-M-9'][1]
print( "Monster M9 count:" + str(monsterCount))

