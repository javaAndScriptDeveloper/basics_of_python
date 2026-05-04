import re
import os

def is_valid_ip(ip_str):
    """
    Функція перевіряє, чи є рядок валідною IPv4-адресою за допомогою регулярного виразу.
    """
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip_str))

def main():
    input_filename = "ips.txt"

    if not os.path.exists(input_filename):
        with open(input_filename, "w", encoding="utf-8") as f:
            f.write("192.168.1.1\n")
            f.write("255.255.255.255\n")
            f.write("256.100.50.0\n")
            f.write("127.0.0\n")
            f.write("not.an.ip.address\n")
            
    print(f"--- Результати перевірки з файлу {input_filename} ---")
    
    try:
        with open(input_filename, "r", encoding="utf-8") as f:
            for line in f:
                ip = line.strip()
                if not ip:
                    continue
                if is_valid_ip(ip):
                    print(f"[{ip}] - Валідна IP-адреса ✅")
                else:
                    print(f"[{ip}] - Невалідна IP-адреса ❌")
                    
    except Exception as e:
        print(f"Помилка при роботі з файлом: {e}")

if __name__ == "__main__":
    main()