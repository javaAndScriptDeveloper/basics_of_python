import json

with open("students.json", encoding="utf-8") as f:
    s1 = json.load(f)

with open("students2.json", encoding="utf-8") as f:
    s2 = json.load(f)

d1 = {s["name"]: s for s in s1}
d2 = {s["name"]: s for s in s2}

names = set(d1) | set(d2)

for name in names:
    if name not in d1 or name not in d2:
        print(name)
    elif d1[name] != d2[name]:
        print(name)