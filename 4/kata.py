
test_dict = {}
skiped = 2

with open('weather.dat', 'r') as weather:
    for line in weather.readlines():
        if skiped > 0:
            skiped -= 1
            continue
        test = line.split()
        if test:
            try:
                test_dict[int(test[0])] = int(test[2].strip('*'))
            except:
                pass
    
    print test_dict