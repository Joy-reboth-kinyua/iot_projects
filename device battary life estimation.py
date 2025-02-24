def battery_life(battery ,consumption_rate):
    hours = 0
    for rate in consumption_rate:
        if battery <= 0:
            break
        battery -= rate
        hours += 1
    return hours

print(battery_life(100, [10,20,15,30,25]))
