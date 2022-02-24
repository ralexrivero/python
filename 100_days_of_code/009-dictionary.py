#!/usr/bin/env python3

"""
Dictionaries
"""


technologies = {
    "c": "Low level programming",
    "Python": "Higer level programming",
    "JavaScript": "Web development language",
    "ReactJs": "JavaScript framework",
    "Java": "Higer level programming",
    "SQL": "Database language",
    "TensorFlow": "Machine Learning platform",
    "html": "Markup language for web structure",
}
# retrieve values from dictionary
print(technologies["ReactJs"])

# adding new values to a dictionary
technologies["CSS"] = "Style language for web design"

print(technologies)

# loop through a dictionary, retrieve keys
for key in technologies:
    print(key)

t = technologies
for key in t:
    print("{:s} = {:s}".format(key, t[key]))
