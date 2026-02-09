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

echo "🔍 Verifying submission 1, variant $VARIANT..."

run_test() {
    local input_data=$1
    local expected_pattern=$2

    output=$(echo -e "$input_data" | timeout 5s python3 main.py 2>&1)
    exit_status=$?

    if [[ $exit_status -eq 124 ]]; then
        echo "⏰ FAIL: Program timed out."
        return 1
    fi

    if [[ "$output" =~ $expected_pattern ]]; then
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
    1) run_test "10\n5" "15" ;;
    2) run_test "10\n5" "5" ;;
    3) run_test "4\n3" "12" ;;
    4)
        run_test "10\n2" "5"
        run_test "10\n0" "[Дд]ілення на нуль неможливе"
        ;;
    5)
        run_test "8" "[Пп]арне"
        run_test "7" "[Нн]епарне"
        ;;
    6) run_test "2\n4\n6" "4" ;;
    7) run_test "10\n3" "1" ;;
    8) run_test "15\n20" "20" ;;
    9) run_test "10\n5" "[Тт]ак|[Єє] дільником" ;;
    10) run_test "0" "32" ;;
esac

exit $?
