def find_max(a, b, c):
    return max(a, b, c)

def main():

    a, b, c = 17, 10, 42
    
    maximum = find_max(a, b, c)
    
    print(f"Числа: {a}, {b}, {c}. Максимум: {maximum}")

if __name__ == "__main__":
    main()