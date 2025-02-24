def door_lock(attempts, correct_pin=7512):
    failed_attempts = 0
    for pin in attempts:
        if pin == correct_pin:
            print( "door unlocked")
            return
    else:
        failed_attempts += 1
        print("Incorrect Pin!")
        if failed_attempts == 3:
            print("Incorrect pin! Locked for 30 secs.")
            time.sleep(30)#simulates lock time.
            failed_attempt = 0 #reset attempts after lockout


door_lock([2021, 7895, 4030, 5043])
door_lock([2021, 7895, 4030, 5043])
door_lock([2021, 7895, 4030, 5043])
door_lock([2021, 7895, 4030, 5043])
door_lock([2021, 7895, 4030, 5043])
door_lock([2603, 5978, 7512])