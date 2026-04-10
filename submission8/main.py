# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
# Оголошення класу CalendarEvent
class CalendarEvent:
    # Конструктор класу
    def __init__(self, title, date, time):
        self.title = title      # назва події
        self.date = date        # дата
        self.time = time        # час

    # Метод для виведення інформації
    def show_event(self):
        print("Подія:", self.title)
        print("Дата:", self.date)
        print("Час:", self.time)

    # Метод для редагування події
    def edit_event(self, new_title=None, new_date=None, new_time=None):
        if new_title:
            self.title = new_title
        if new_date:
            self.date = new_date
        if new_time:
            self.time = new_time


# Створення події
event1 = CalendarEvent("Зустріч", "10.04.2026", "14:00")

print("Початкові дані:")
event1.show_event()

# Редагування події
event1.edit_event(new_title="Зустріч з викладачем", new_time="15:00")

print("\nПісля редагування:")
event1.show_event()