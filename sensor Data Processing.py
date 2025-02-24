def process_temperature_data(temps):
    """calculate the average maximum and minimum values"""
    avg_temp = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)

    return{
        "average_temperature": round(avg_temp, 2) ,
        "max_temperature": max_temp,
        "min_temperature": min_temp

}


temps = [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 51]
results = process_temperature_data(temps)
print(results)
