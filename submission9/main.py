import re
import sys


def solve():
    try:
        input_text = sys.stdin.read().strip()
        if not input_text:
            return

        date_pattern = r"(\d{2})-(\d{2})-(\d{4})"
        replacement = r"\3-\2-\1"
        result = re.sub(date_pattern, replacement, input_text)
        print(result)

    except EOFError:
        pass

if __name__ == "__main__":
    solve()