import json
import pandas as pd
import os

# 1. Робота з JSON
if os.path.exists('students.json'):
    with open('students.json', 'r', encoding='utf=8') as f:
        data_json = json.load(f)

    data_json.append({"name": "Тестовий Студент", "age": 20, "faculty": "ІТ" })

    with open('updated_students.json', 'w', encoding='utf=8') as f:
        json.dump(data_json, f, ensure_ascii=False, indent=4)

# 2. Робота з CSV
df_csv = (pd.DataFrame({
    'Продукт': ['Яблуко', 'Банан'],
    'Ціна': [30, 50]
}))
df_csv.to_csv('products.csv', index=False)

df_csv.loc[len(df_csv)] = ['Груша', 45]
df_csv.to_csv('updated_products.csv', index=False)

# 3. Робота з Excel
df_staff = pd.DataFrame({
    'Ім’я': ['Аня', 'Ігор', 'Катя'],
    'Зарплата': [15000, 28000, 12000]
})
df_staff.to_excel('staff.xlsx', index=False)
df_excel = pd.read_excel('staff.xlsx')
processed = df_excel[df_excel['Зарплата'] > 13000].sort_values(by='Зарплата')
processed.to_excel('processed_staff.xlsx', index=False)

#ІНДИВІДУАЛЬНЕ ЗАВДАННЯ

if os.path.exists('students.json'):
    with open('students.json', 'r', encoding='utf-8') as f:
        students = json.load(f)

        for s in students:
            print(f"{s['name']} (Вік: {s['age']}, Факультет: {s['faculty']})")
else:
    print("Файл students.json не знайдено ")
