def find_station(stations, name):
    for i in range(len(stations)):
        if stations[i] == name:
            return i
    
    return 

def count_stops(stations, start, stop):
    start_index = find_station(stations, start)
    stop_index = find_station(stations, stop)
    if start_index == None or stop_index == None:
        return -1
    else:
        if start_index < stop_index:
            return stop_index - start_index
        else:
            return start_index - stop_index
        