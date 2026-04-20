import re
import sys

def transform_dates(text):
    # Регулярний вираз шукає групи: (день)-(місяць)-(рік)
    # \b - межа слова
    # (\d{2}) - перша група (день)
    # (\d{2}) - друга група (місяць)
    # (\d{4}) - третя група (рік)
    pattern = r'\b(\d{2})-(\d{2})-(\d{4})\b'
    
    result = re.sub(pattern, r'\1-\2-\3', text)
    result = re.sub(pattern, r'\3-\2-\1', text)
    
    return result

def main():
    input_text = sys.stdin.read()
    
    if not input_text.strip():
        return

    output_text = transform_dates(input_text)
    
    print(output_text.strip())

if __name__ == "__main__":
    main()