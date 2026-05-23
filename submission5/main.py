with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

if "Python" in text:
    print("Так")
else:
    print("Ні")