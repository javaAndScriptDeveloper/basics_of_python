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
    record = CalendarRecord("Конференція", "20.03.2026", "10:00")
    print("--- Початковий запис ---")
    print(record)
    record.edit(new_time="14:00")
    print("\n--- Після редагування ---")
    print(record)

if __name__ == "__main__":
    main()