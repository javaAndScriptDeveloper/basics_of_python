#!/bin/bash

VARIANT_FILE="variant.txt"

if [[ ! -f "$VARIANT_FILE" ]]; then
    echo "❌ Error: $VARIANT_FILE not found."
    exit 1
fi

VARIANT=$(head -n 1 "$VARIANT_FILE" | xargs)

if [[ -z "$VARIANT" ]]; then
    echo "⚠️ Error: $VARIANT_FILE is empty."
    exit 1
fi

if ! [[ "$VARIANT" =~ ^[1-9]$|^10$ ]]; then
    echo "🚫 Exception: Invalid variant '$VARIANT'. Must be between 1 and 10."
    exit 1
fi

echo "🔍 Verifying submission 9, variant $VARIANT..."

# Check that regex module is used
if ! grep -qE "import re|from re " main.py; then
    echo "❌ FAIL: main.py must use regular expressions (no 'import re' found)."
    exit 1
fi
echo "✅ Regex check: 're' module imported in main.py."

run_test() {
    local input_data=$1
    local expected_pattern=$2

    output=$(echo -e "$input_data" | timeout 5s python3 main.py 2>&1)
    exit_status=$?

    if [[ $exit_status -eq 124 ]]; then
        echo "⏰ FAIL: Program timed out."
        return 1
    fi

    normalized=$(echo "$output" | tr '\n' ' ')

    if [[ "$normalized" =~ $expected_pattern ]]; then
        echo "✅ PASS: Output matches expected pattern."
        return 0
    else
        echo "❌ FAIL: Output did not match."
        echo "📤 Expected pattern: $expected_pattern"
        if [[ -z "$output" ]]; then
            echo "📥 Received: [Empty Output]"
        else
            echo "📥 Received: $output"
        fi
        return 1
    fi
}

case $VARIANT in
    1)
        # Заміна всіх цифр на #
        run_test "abc123def456" "abc###def###" || exit 1
        run_test "no digits here" "no digits here"
        ;;
    2)
        # Пошук електронних адрес у тексті
        run_test "Contact user@example.com for info" "user@example.com" || exit 1
        run_test "No emails here" "[Нн]е знайден|[Нн]емає|[Пп]орожн|\[\]"
        ;;
    3)
        # Видалення зайвих пробілів
        run_test "Hello   world   test" "Hello world test" || exit 1
        run_test "  spaces   everywhere  " "spaces +everywhere"
        ;;
    4)
        # Пошук слів з великої літери
        run_test "Hello world Python is Great" "Hello.*Python.*Great" || exit 1
        run_test "all lowercase here" "[Нн]е знайден|[Нн]емає|[Пп]орожн|\[\]"
        ;;
    5)
        # Перевірка коректності телефонного номера
        p5v="[Кк]оректн|[Вв]ірн|[Вв]алідн|[Пп]равильн|True|valid"
        run_test "+380501234567" "$p5v" || exit 1
        p5i="[Нн]екоректн|[Нн]евірн|[Нн]евалідн|[Нн]еправильн|False|invalid"
        run_test "abc123" "$p5i"
        ;;
    6)
        # Видалення небажаних символів
        run_test "Hello! @World# \$Test%" "Hello.*World.*Test" || exit 1
        run_test "Clean text" "Clean text"
        ;;
    7)
        # Пошук всіх email-адрес у тексті
        run_test "Send to a@b.com and c@d.org" "a@b\.com.*c@d\.org|c@d\.org.*a@b\.com" || exit 1
        run_test "No emails" "[Нн]е знайден|[Нн]емає|[Пп]орожн|\[\]"
        ;;
    8)
        # Заміна дат dd-mm-yyyy на yyyy-mm-dd
        run_test "Date: 25-12-2024" "2024-12-25" || exit 1
        run_test "Events: 01-06-2023 and 15-03-2025" "2023-06-01.*2025-03-15"
        ;;
    9)
        # Перевірка валідності IP-адреси
        p9v="[Кк]оректн|[Вв]ірн|[Вв]алідн|[Пп]равильн|True|valid"
        run_test "192.168.1.1" "$p9v" || exit 1
        p9i="[Нн]екоректн|[Нн]евірн|[Нн]евалідн|[Нн]еправильн|False|invalid"
        run_test "999.999.999.999" "$p9i"
        ;;
    10)
        # Заміна пробілів на підкреслення
        run_test "Hello World Test" "Hello_World_Test" || exit 1
        run_test "NoSpaces" "NoSpaces"
        ;;
esac

exit $?
