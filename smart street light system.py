def street_light(light_level, motion):
    if light_level < 30 and motion:
        return "Streetlight ON"
    else:
        return "StreetlightOFF"

print(street_light(48, True))

