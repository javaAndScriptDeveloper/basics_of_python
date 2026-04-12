def main():
    try:
        year = int(input())
        
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("Рік високосний")
        else: 
            print("Рік звичайний")
            
    except ValueError:
        print("Помилка: Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()