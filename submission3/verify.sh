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

echo "🔍 Verifying submission 3, variant $VARIANT..."

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
    1) run_test "" "45" ;;
    2) run_test "" "6" ;;
    3) run_test "" "12.*7.*3.*28.*15.*9.*33.*21" ;;
    4) run_test "" "21.*33.*9.*15.*28.*3.*45.*7.*12" ;;
    5) run_test "" "22" ;;
    6) run_test "" "[Тт]ак|[Іі]снує|[Зз]найден|[Пп]рисутн|True" ;;
    7) run_test "" "3.*7.*9.*12.*15.*21.*28.*33.*45" ;;
    8) run_test "" "[Нн]і|[Нн]е.*однаков|[Рр]ізн|False" ;;
    9) run_test "" "12.*7.*45.*3.*28.*15.*9.*33.*21.*50.*60.*70" ;;
    10) run_test "" "4.*2.*7.*9.*1.*3|1.*2.*3.*4.*7.*9" ;;
esac

exit $?
