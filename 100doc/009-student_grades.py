#!/usr/bin/env python3

scores = {
    "John": 75,
    "Ronald": 99,
    "Clarck": 78,
    "Mark": 69,
    "Newton": 82,
}

grades = {}

for name in scores:
    score = scores[name]
    if score > 90:
        grades[name] = "Outstanding"
    elif score > 80:
        grades[name] = "Exceeds Expectations"
    elif score > 70:
        grades[name] = "Acceptable"
    else:
        grades[name] = "Fail"

for key in grades:
    print("{:s}: {:s}".format(key, grades[key]))
