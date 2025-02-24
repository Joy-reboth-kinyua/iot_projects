def fire_alarm(temps, smoke):
         if temps> 60 and smoke >5:
             return "fire detected! Alarm Triggered!"
         else:
             return "normal condition. No alarm."


print(fire_alarm(65, 6))
