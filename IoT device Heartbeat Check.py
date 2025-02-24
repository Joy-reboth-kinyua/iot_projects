def device_offline(timestamps, T):
    for i in range(1, len(timestamps)):  #start from the second timestamp
        if timestamps[i] - timestamps[i-1] > T: #if the gap between two consecutive timestamps is greater than T,we return true
            return True #device went offline
    return False #device remained online
           #if we finish the loop without finding a gap, we return false
timestamps = [0,3,6,15,18]
T = 5
print(device_offline(timestamps, T))

