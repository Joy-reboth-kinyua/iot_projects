def smart_fridge(temps):
    if temps <2 or temps >8:
        return"warning! temperature too high!"

    else:
        return"Temperature is stable."


print(smart_fridge(5))
print(smart_fridge(1))