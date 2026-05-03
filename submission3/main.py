def main():
    try:
        list1 = input().split()
        list2 = input().split()

        combined_list = list1 + list2

        print(combined_list)

    except EOFError:
        print("Помилка: Недостатньо даних для вводу")
    except Exception as e:
        print(f"Сталася неочікувана помилка: {e}")

if __name__ == "__main__":
    main()