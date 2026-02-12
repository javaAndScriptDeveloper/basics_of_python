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

echo "🔍 Verifying submission 4, variant $VARIANT..."

run_test() {
    local input_data=$1
    local expected_pattern=$2

    output=$(echo -e "$input_data" | timeout 5s python3 main.py 2>&1)
    exit_status=$?

    if [[ $exit_status -eq 124 ]]; then
        echo "⏰ FAIL: Program timed out."
        return 1
    fi

    # Normalize multiline output to single line for pattern matching
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
    1) run_test "" "16.*34.*13" ;;
    2) run_test "" "120.*40320" ;;
    3) run_test "" "32.*212.*98" ;;
    4) run_test "" "1000.*5500.*250" ;;
    5) run_test "" "120.*330.*15" ;;
    6) run_test "" "25.*200" ;;
    7) run_test "" "25.*144.*49" ;;
    8) run_test "" "17.*10.*42" ;;
    9) run_test "" "2.54.*25.4.*12.7" ;;
    10) run_test "" "3.*5.*6" ;;
esac

exit $?
