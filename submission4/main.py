# Реалізуйте функцію для вашого варіанту та викличте її для тестових значень
# Виведіть результат кожного виклику за допомогою print()
import re



def golosniliteri(ryadok):
    if type(ryadok) is not str:
        print("Your ryadok is not a string type")
        return -1

    l = re.findall(r"[aeiou]+?", str(ryadok).lower())
    return len(l)

print(golosniliteri("hello world"))
print(golosniliteri("education"))
print(golosniliteri("beautiful day"))
# 10) Кількість голосних: "hello world", "education", "beautiful day"
