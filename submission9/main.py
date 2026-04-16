# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
import re
import sys

def is_valid_ip(ip):
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return False
    
    parts = ip.split('.')
    for part in parts:
        if not 0 <= int(part) <= 255:
            return False
    return True

def main():
    input_data = sys.stdin.read().strip()
    
    if not input_data:
        return

    if is_valid_ip(input_data):
        print(f"IP {input_data} is valid")
    else:
        print(f"IP {input_data} is invalid")

if __name__ == "__main__":
    main()