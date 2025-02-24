def bulb_turn_off_time(sunset, n):
    return (sunset + n)% 24  #ensure it wraps around 24 hours

print(bulb_turn_off_time(18, 6)) #output:0(midnight)
print(bulb_turn_off_time(22, 5)) #outputs:3(3 am)
