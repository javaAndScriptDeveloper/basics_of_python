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

echo "🔍 Verifying submission 5, variant $VARIANT..."

run_program() {
    output=$(timeout 5s python3 main.py 2>&1)
    exit_status=$?

    if [[ $exit_status -eq 124 ]]; then
        echo "⏰ FAIL: Program timed out."
        return 1
    fi

    if [[ $exit_status -ne 0 ]]; then
        echo "❌ FAIL: Program exited with error."
        if [[ -n "$output" ]]; then
            echo "📥 Output: $output"
        fi
        return 1
    fi

    return 0
}

check_file() {
    local file=$1
    local expected_pattern=$2

    if [[ ! -f "$file" ]]; then
        echo "❌ FAIL: File '$file' not found."
        return 1
    fi

    local content
    content=$(cat "$file" | tr '\n' ' ')

    if [[ "$content" =~ $expected_pattern ]]; then
        echo "✅ PASS: Output matches expected pattern."
        return 0
    else
        echo "❌ FAIL: File content did not match."
        echo "📤 Expected pattern: $expected_pattern"
        echo "📥 File content: $content"
        return 1
    fi
}

check_result() {
    local expected_pattern=$1
    local normalized
    normalized=$(echo "$output" | tr '\n' ' ')

    if [[ "$normalized" =~ $expected_pattern ]]; then
        echo "✅ PASS: Output matches expected pattern."
        return 0
    fi

    if [[ -f "output.txt" ]]; then
        local file_content
        file_content=$(cat "output.txt" | tr '\n' ' ')
        if [[ "$file_content" =~ $expected_pattern ]]; then
            echo "✅ PASS: File content matches expected pattern."
            return 0
        fi
    fi

    echo "❌ FAIL: Result not found in stdout or output.txt."
    echo "📤 Expected pattern: $expected_pattern"
    if [[ -z "$output" ]]; then
        echo "📥 stdout: [Empty]"
    else
        echo "📥 stdout: $output"
    fi
    if [[ -f "output.txt" ]]; then
        echo "📥 output.txt: $(cat output.txt)"
    fi
    return 1
}

# Clean up previous test files
rm -f input.txt output.txt

case $VARIANT in
    1)
        printf "Hello World\nPython Programming\nFile Operations\n" > input.txt
        run_program || exit 1
        check_file "output.txt" "[Hh]ello.*[Oo]perations"
        ;;
    2)
        printf "Hello World\nPython Programming\nFile Operations\n" > input.txt
        run_program || exit 1
        check_file "output.txt" "6"
        ;;
    3)
        printf "10\n20\n30\n40\n50\n" > input.txt
        run_program || exit 1
        check_result "30"
        ;;
    4)
        printf "First line\nSecond line\nThird line\n" > input.txt
        run_program || exit 1
        check_file "output.txt" "Third.*Second.*First"
        ;;
    5)
        printf "Hello World\nPython Programming\nFile Operations\n" > input.txt
        run_program || exit 1
        check_result "[Тт]ак|[Зз]найден|[Іі]снує|[Пп]рисутн|True"
        ;;
    6)
        printf "Hello World\nPython Programming\n" > input.txt
        run_program || exit 1
        check_file "output.txt" "Ukraine"
        ;;
    7)
        printf "Line 1\nLine 2\n" > input.txt
        run_program || exit 1
        check_file "input.txt" "Новий рядок додано"
        ;;
    8)
        printf "45\n12\n78\n3\n56\n" > input.txt
        run_program || exit 1
        check_file "output.txt" "3.*12.*45.*56.*78"
        ;;
    9)
        printf "Line 1\n\nLine 2\n\n\nLine 3\n" > input.txt
        run_program || exit 1
        check_file "output.txt" "Line 1.*Line 2.*Line 3"
        ;;
    10)
        printf "Old content\n" > input.txt
        run_program || exit 1
        check_file "input.txt" "Файл перезаписано"
        ;;
esac

exit $?
