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
    'RANGE-S-8' : 420,
    'FLY-S-8' : 20,
    
    'MELEE-S-9' : 225,
    'MOUNT-S-9' : 112,
    'RANGE-S-9' : 220,
    'FLY-S-9' : 10,
    
    'MELEE-G-8' : 360,
    'MOUNT-G-8' : 175,
    'RANGE-G-8' : 345,
    'FLY-G-8' : 17,

    'MELEE-G-9' : 185,
    'MOUNT-G-9' : 90,
    'RANGE-G-9' : 175,
    'FLY-G-9' : 8
    
}

kill_1 = 'MELEE'
kill_2 = 'FLY'
kill_3 = 'MOUNT'
kill_4 = 'RANGE'

# for a 250 multiplier I did 170 M9 and 350 M8 and up to 500 M7
factor = 275
for key,value in countLookup.items():
    count = value*factor
    print(key + ":" + str(count))

