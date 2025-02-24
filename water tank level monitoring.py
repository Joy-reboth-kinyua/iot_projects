def check_tank_level(levels):
    for level in levels:
        if level < 30:
             return "Refill needed"
        else:
            return "Tank ok"

print(check_tank_level([50, 45, 32,28,40]))
print(check_tank_level([70,80,90,65,45,60]))