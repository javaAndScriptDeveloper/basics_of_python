# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
import sys

class CalendarEntry:
    def __init__(self, date, event_description):
        self.date = date
        self.event_description = event_description
        
    def edit_event(self, new_description):
        self.event_description = new_description
        
    def show_entry(self):
        print(f"{self.date} {self.event_description}")

input_data = sys.stdin.read().splitlines()

if len(input_data) >= 2:
    date_input = input_data[0]
    event_input = input_data[1]
    
    my_entry = CalendarEntry(date_input, event_input)
    my_entry.show_entry()
else:
    date_input = input("Введіть дату (наприклад, 15.01.2026): ")
    event_input = input("Введіть подію: ")
    my_entry = CalendarEntry(date_input, event_input)
    my_entry.show_entry()