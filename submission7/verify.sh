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

echo "🔍 Verifying submission 7, variant $VARIANT..."

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

# Clean up previous test files
rm -f input.txt error.log

case $VARIANT in
    1)
        run_test "10\n5" "2" || exit 1
        p1="[Дд]ілення на нуль|[Пп]омилк.*нуль|ZeroDivisionError"
        run_test "10\n0" "$p1"
        ;;
    2)
        run_test "42" "42" || exit 1
        p2="[Нн]е є цілим|[Пп]омилк|[Нн]екоректн|ValueError"
        run_test "abc" "$p2"
        ;;
    3)
        run_test "5 10 15" "5.*10.*15" || exit 1
        run_test "" "[Пп]орожн|[Пп]омилк|[Сс]писок|[Нн]емає"
        ;;
    4)
        run_test "5" "[Дд]одатн|5" || exit 1
        run_test "-3" "[Вв]ід.*ємн|[Пп]омилк|[Нн]егативн"
        ;;
    5)
        # Test 1: file exists
        printf "Hello World\nPython Programming\n" > input.txt
        output=$(timeout 5s python3 main.py 2>&1)
        if [[ $? -eq 124 ]]; then
            echo "⏰ FAIL: Program timed out."
            exit 1
        fi
        normalized=$(echo "$output" | tr '\n' ' ')
        if [[ "$normalized" =~ Hello|Python ]]; then
            echo "✅ PASS: File read successfully."
        else
            echo "❌ FAIL: File content not found in output."
            echo "📥 Received: $output"
            exit 1
        fi
        # Test 2: file missing
        rm -f input.txt
        output=$(timeout 5s python3 main.py 2>&1)
        if [[ $? -eq 124 ]]; then
            echo "⏰ FAIL: Program timed out."
            exit 1
        fi
        normalized=$(echo "$output" | tr '\n' ' ')
        p5="[Пп]омилк|[Фф]айл.*не|FileNotFoundError|[Нн]е існує|[Нн]е знайден"
        if [[ "$normalized" =~ $p5 ]]; then
            echo "✅ PASS: File error handled correctly."
        else
            echo "❌ FAIL: File error not handled."
            echo "📥 Received: $output"
            exit 1
        fi
        ;;
    6)
        run_test "name" "Олена" || exit 1
        p6="[Кк]люч.*не знайден|KeyError|[Пп]омилк|[Нн]емає"
        run_test "address" "$p6"
        ;;
    7)
        run_test "42" "42" || exit 1
        run_test "abc" "[Пп]омилк|[Нн]еможливо|[Нн]екоректн|ValueError"
        ;;
    8)
        run_test "10\n5" "2" || exit 1
        rm -f error.log
        p8="[Пп]омилк|[Дд]ілення на нуль|ZeroDivisionError"
        run_test "10\n0" "$p8" || exit 1
        if [[ -f "error.log" ]] && [[ -s "error.log" ]]; then
            echo "✅ PASS: error.log contains error information."
        else
            echo "❌ FAIL: error.log not found or empty after error."
            exit 1
        fi
        ;;
    9)
        # Test 1: correct format (name:age per line)
        printf "Олена:20\nІван:22\nМарія:19\n" > input.txt
        output=$(timeout 5s python3 main.py 2>&1)
        if [[ $? -eq 124 ]]; then
            echo "⏰ FAIL: Program timed out."
            exit 1
        fi
        normalized=$(echo "$output" | tr '\n' ' ')
        if [[ "$normalized" =~ Олена.*Іван.*Марія ]]; then
            echo "✅ PASS: Correctly formatted data processed."
        else
            echo "❌ FAIL: Correct format not processed."
            echo "📥 Received: $output"
            exit 1
        fi
        # Test 2: incorrect format
        printf "Олена:abc\nІван:22\n" > input.txt
        output=$(timeout 5s python3 main.py 2>&1)
        if [[ $? -eq 124 ]]; then
            echo "⏰ FAIL: Program timed out."
            exit 1
        fi
        normalized=$(echo "$output" | tr '\n' ' ')
        if [[ "$normalized" =~ [Пп]омилк|[Фф]ормат|[Нн]екоректн|ValueError ]]; then
            echo "✅ PASS: Format error handled correctly."
        else
            echo "❌ FAIL: Format error not handled."
            echo "📥 Received: $output"
            exit 1
        fi
        ;;
    10)
        run_test "25-12-2024" "[Кк]оректн|[Вв]ірн|[Пп]равильн|25.12.2024" || exit 1
        run_test "31-02-2024" "[Нн]екоректн|[Пп]омилк|[Нн]евірн|[Нн]еправильн"
        ;;
esac

exit $?
