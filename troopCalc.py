print("hello world")
print("hello shane")

totalLeadership = 50000;

# the lookup is strength, health, leadership
statLookup = {
    'MELEE-G-9' : (5510,16530,1),
    'MELEE-G-8' : (3060,9180,1)
}

countLookup = {
    'MELEE-S-8' : 440,
    'MOUNT-S-8' : 215,
    'FLY-S-8' : 20,
    'RANGE-S-8' : 295,
    'MELEE-S-9' : 220,
    'MOUNT-S-9' : 110,
    'FLY-S-9' : 11,
    'RANGE-S-9' : 210,
    'MELEE-G-8' : 390,
    'MOUNT-G-8' : 195,
    'FLY-G-8' : 18,
    'RANGE-G-8' : 380,
    'MELEE-G-9' : 200,
    'MOUNT-G-9' : 100,
    'FLY-G-9' : 9,
    'RANGE-G-9' : 200
}

kill_1 = 'MELEE'
kill_2 = 'FLY'
kill_3 = 'MOUNT'
kill_4 = 'RANGE'

print(statLookup['MELEE-G-9'][0])
