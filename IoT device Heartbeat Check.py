def device_offline(timestamps, T):
    for i in range(1, len(timestamps)):  #start from the second timestamp
        if timestamps[i] - timestamps[i-1] > T:
            return True #device went offline
        return False #device remained online

