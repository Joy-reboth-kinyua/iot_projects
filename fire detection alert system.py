def fire_detection_alert(sensor_data):
    for temp, smoke, gas in sensor_data:
        if temp >50 and smoke>70 and gas >80:
            return True #fire detected
    return False#no fire detected

sensor_data = [(45, 50, 60), (55,80,90), (30, 40, 30)]
results = fire_detection_alert(sensor_data)
print(str(results) + "( fire detected at index 1 ) ")