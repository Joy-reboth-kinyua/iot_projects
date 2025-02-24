def motion_alert(readings):
        if 1 in readings:
            return "alert!"
        else:
            return "safe"

print(motion_alert([0,0,1,0])) #output:"alert'
print(motion_alert([0,0,0,0])) #output:"safe"