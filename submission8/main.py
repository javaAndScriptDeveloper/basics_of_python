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
    record1 = CalendarRecord("Зустріч", "15.01.2026", "10:00")
    record2 = CalendarRecord("Конференція", "20.03.2026", "12:00")
    print("--- Початкові записи ---")
    print(record1)
    print(record2)
    record1.edit(new_time="11:30")
    print("\n--- Після редагування ---")
    print(record1)
    print(record2)

if __name__ == "__main__":
    main()