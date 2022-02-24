#!/usr/bin/env python3
""" dictionay methods """

device = {
    'type': 'Phone',
    'brand': 'Samsung',
    'size': '7"',
    'year': 2021
}

print('type' in device)
print('type' in device.keys())
print('type' in device.values())
print(2021 in device.values())

""" items grabs the entire item (the key/value pair) """

print(device.items())

""" search for items like a tuple """
print(('type', 'Phone') in device.items())

device2 = device.copy()

device.clear()
print(device)
print(device2)

""" pop returns the value removed """
print(device2.pop('size'))
print(device2)

""" update or create a new item (key/value pair) if it doesn't exist """
device2.update({'brand': 'Samsung Galaxy', 'color': 'black'})
print(device2)