from datetime import datetime

date_str = input()

try:
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    print(date_obj.strftime("%d.%m.%Y"))
except ValueError:
    print("Некоректна дата")