print("--------------TROOP CALCULATOR-----------------------")

leadership = 248000

# the lookup is strength, health, leadership
statLookup = {
    'MELEE-G-9' : (5510,16530,1),
    'MELEE-G-8' : (3060,9180,1)
}

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

for key,value in percentLookup.items():
    count = (leadership*value)/countLookup[key][1]
    print(key + ":" + str(round(count)))

