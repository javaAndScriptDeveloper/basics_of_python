import json
import pandas as pd

#Для JSON
with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f) #

students = [student for student in students if student["name"] != "Петро"] #Видалення Петра

with open("students_updated.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

print("Студента 'Петро' видалено.")


#Для CSV
df = pd.read_csv("students.csv") #Знаходимо файл
df = df[df["name"] != "Петро"] #Видалення Петра зі списку як демонстрація функції видалення
df.to_csv("students_updated.csv", index=False, encoding="utf-8-sig") #Запис оновленого списку у новий файл


# Для Excel
excel_file = "students.xlsx"
df = pd.read_excel(excel_file, header=0)  # Перший рядок стає заголовком

print("Початкові дані Excel:") #Виводимо в термінал через проблеми з PyCharm
print(df)

# Фільтруємо за віком >= 20
df_filtered = df[df["Вік"] >= 20]

# Сортуємо за ім'ям
df_filtered = df_filtered.sort_values(by="Ім'я")

print("\nОброблені дані Excel:")
print(df_filtered)

# Зберігаємо результат
output_file = "students_updated.xlsx"
df_filtered.to_excel(output_file, index=False)

print(f"\nОброблені дані збережено у файл: {output_file}") #Виводимо в термінал через проблеми з PyCharm