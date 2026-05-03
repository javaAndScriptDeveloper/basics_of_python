def inches_to_cm(inches):
    """
    Функція приймає значення в дюймах і повертає сантиметри.
    """
    return inches * 2.54

def main():
    test_values = [1, 10, 5]
    for val in test_values:
        print(inches_to_cm(val))

if __name__ == "__main__":
    main()