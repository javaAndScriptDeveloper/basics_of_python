import os

#Вхідні дані
input_file = "input.txt"
output_file = "output.txt"
word_to_find = "Python"

#Перевірка існування файлу
if not os.path.exists(input_file):
    print("Файл не існує!")
else:
    # Зчитування даних
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    #Перетворення у нижній регістр
    text_lower = text.lower()

    #Запис у новий файл
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text_lower)

    print("Дані записано у новий файл.")

    #Перевірка наявності слова
    if word_to_find.lower() in text_lower:
        print(f"Слово '{word_to_find}' знайдено у файлі.")
    else:
        print(f"Слово '{word_to_find}' не знайдено у файлі.")
