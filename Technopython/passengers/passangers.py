def process(data, events, car):

    print(data)
    for event in events:    #проход по событиям
        if event["type"] == "walk": #если текущее событие - хождение пассажира
            counter = -1
            persons_car = -1
            for car in data[0]["cars"]: #проход по вагонам
                counter += 1
                if event["passenger"] in car["people"]: #если пассажир из данного вагона
                    persons_car = counter               #запоминаем вагон
                    del(car["people"][car["people"].index(event["passenger"])])
                    break
            if persons_car != -1:
                data[0]["cars"][persons_car + event["distance"]]["people"].append(event["passenger"])
            print(data)

            #if i["type"] == "switch":
    '''
        ТУТ ДОЛЖЕН БЫТЬ ВАШ КОД
    '''
    return -1
