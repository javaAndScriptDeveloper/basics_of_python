class CalendarRecord:
    def __init__(self, title, date, time):
        self.title = title
        self.date = date
        self.time = time
    def edit(self, new_title=None, new_date=None, new_time=None):
        if new_title is not None:
            self.title = new_title
        if new_date is not None:
            self.date = new_date
        if new_time is not None:
            self.time = new_time
    def __str__(self):
        return f"📅 {self.date} о {self.time} | {self.title}"


def main():
    record1 = CalendarRecord("Лекція з Баз Даних", "2026-05-15", "10:00")
    record2 = CalendarRecord("Зустріч по проекту", "2026-05-16", "14:30")
    print("--- Початкові записи в календарі ---")
    print(record1)
    print(record2)
    print("\n--- Відбулися зміни у розкладі ---")
    record1.edit(new_time="12:00", new_title="Лекція з Баз Даних (Перенесено)")
    print("\n--- Оновлені записи в календарі ---")
    print(record1)
    print(record2)

if __name__ == "__main__":
    main()