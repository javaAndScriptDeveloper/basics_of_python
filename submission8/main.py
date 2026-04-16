# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
import sys

class CalendarEvent:
    def __init__(self, date: str, title: str):
        self.date = date
        self.title = title

    def display_event(self):
        print(f"Подія: {self.title}, Дата: {self.date}")

def main():
    input_data = sys.stdin.read().splitlines()
    
    if len(input_data) < 2:
        return

    date_input = input_data[0].strip()
    title_input = input_data[1].strip()

    event = CalendarEvent(date_input, title_input)
    event.display_event()

if __name__ == "__main__":
    main()