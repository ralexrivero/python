#!/usr/bin/env python3

# nesting dictionary in a list

carrer_log = [
    {
        "Fundations": "low level programming",
        "Languages": ["C", "Assembly"],
        "Projects": 2
    },
    {
        "Fundations": "Higer level programming",
        "Languages": ["Python", "Ruby"],
        "Projects": 4
    },
]

print(carrer_log)

print("\n", "*" * 80, "\n")


def add_new_level(fundations, languages, projects):
    new_dict = {}
    new_dict["Fundations"] = fundations
    new_dict["Languages"] = [languages]
    new_dict["Projects"] = projects
    carrer_log.append(new_dict)


add_new_level("Web services", ["SQL", "NGINX", "PHP", "JavaScript"], 5)

print(carrer_log)
