def water_leakage(moisture_level):
    if moisture_level > 70:
        return "Water leakage detected!"
    else:
        return"no leakages"

print(water_leakage(80))