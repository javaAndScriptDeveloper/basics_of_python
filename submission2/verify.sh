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

echo "🔍 Verifying submission 2, variant $VARIANT..."

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
    1) run_test "2\n3\n5" "2.*5.*8.*11.*14" ;;
    2) run_test "5" "120" ;;
    3) run_test "1\n20" "2.*3.*5.*7.*11.*13.*17.*19" ;;
    4) run_test "20" "1.*1.*2.*3.*5.*8.*13" ;;
    5)
        run_test "5" "[Дд]одатн"
        run_test "-3" "[Вв]ід.*ємн"
        ;;
    6) run_test "3\n7\n5" "7" ;;
    7) run_test "" "1.*2.*4.*5.*98.*100" ;;
    8) run_test "5" "5.*10.*15.*20.*25.*30.*35.*40.*45.*50" ;;
    9)
        run_test "2024" "[Вв]исокосний"
        run_test "2023" "[Нн]е.*високосний"
        ;;
    10) run_test "3\n2\n5" "3.*6.*12.*24.*48" ;;
esac

exit $?
