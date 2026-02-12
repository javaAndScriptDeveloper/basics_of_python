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

echo "🔍 Verifying submission 6, variant $VARIANT..."

run_program() {
    output=$(timeout 10s python3 main.py 2>&1)
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

check_json() {
    local file=$1
    local expected_pattern=$2

    if [[ ! -f "$file" ]]; then
        echo "❌ FAIL: File '$file' not found."
        return 1
    fi

    # Re-serialize JSON with ensure_ascii=False for reliable Cyrillic matching
    local content
    content=$(python3 -c "
import json, sys
with open('$file', encoding='utf-8') as f:
    data = json.load(f)
print(json.dumps(data, ensure_ascii=False))
" 2>/dev/null | tr '\n' ' ')

    if [[ -z "$content" ]]; then
        content=$(cat "$file" | tr '\n' ' ')
    fi

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

check_stdout() {
    local expected_pattern=$1
    local normalized
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

check_result() {
    local expected_pattern=$1
    local normalized
    normalized=$(echo "$output" | tr '\n' ' ')

    if [[ "$normalized" =~ $expected_pattern ]]; then
        echo "✅ PASS: Output matches expected pattern."
        return 0
    fi

    if [[ -f "output.json" ]]; then
        local content
        content=$(python3 -c "
import json
with open('output.json', encoding='utf-8') as f:
    data = json.load(f)
print(json.dumps(data, ensure_ascii=False))
" 2>/dev/null | tr '\n' ' ')
        if [[ -z "$content" ]]; then
            content=$(cat "output.json" | tr '\n' ' ')
        fi
        if [[ "$content" =~ $expected_pattern ]]; then
            echo "✅ PASS: File content matches expected pattern."
            return 0
        fi
    fi

    echo "❌ FAIL: Result not found in stdout or output.json."
    echo "📤 Expected pattern: $expected_pattern"
    if [[ -z "$output" ]]; then
        echo "📥 stdout: [Empty]"
    else
        echo "📥 stdout: $output"
    fi
    return 1
}

create_students_json() {
    cat > students.json << 'JSONEOF'
[
    {"name": "Олена", "age": 20, "faculty": "КН"},
    {"name": "Іван", "age": 22, "faculty": "ІТ"},
    {"name": "Марія", "age": 19, "faculty": "КН"},
    {"name": "Петро", "age": 21, "faculty": "ФМ"},
    {"name": "Анна", "age": 23, "faculty": "ІТ"}
]
JSONEOF
}

# Clean up previous test files
rm -f students.json students2.json students.csv output.json

case $VARIANT in
    1)
        create_students_json
        run_program || exit 1
        check_stdout "Олена.*Іван.*Марія.*Петро.*Анна"
        ;;
    2)
        create_students_json
        run_program || exit 1
        check_json "output.json" "Сергій"
        ;;
    3)
        create_students_json
        run_program || exit 1
        check_stdout "Марія.*(19|КН)"
        ;;
    4)
        create_students_json
        run_program || exit 1
        check_json "output.json" "Іван.*22.*КН"
        ;;
    5)
        create_students_json
        run_program || exit 1
        check_json "output.json" "Олена.*Анна"
        ;;
    6)
        create_students_json
        run_program || exit 1
        check_json "output.json" "Марія.*Олена.*Петро.*Іван.*Анна"
        ;;
    7)
        create_students_json
        run_program || exit 1
        check_result "21"
        ;;
    8)
        run_program || exit 1
        check_json "output.json" "програмування.*Бази даних.*Алгоритми"
        ;;
    9)
        cat > students.csv << 'CSVEOF'
name,age,faculty
Олена,20,КН
Іван,22,ІТ
Марія,19,КН
Петро,21,ФМ
Анна,23,ІТ
CSVEOF
        run_program || exit 1
        check_json "output.json" "Олена.*Іван.*Марія"
        ;;
    10)
        create_students_json
        cat > students2.json << 'JSONEOF'
[
    {"name": "Олена", "age": 21, "faculty": "КН"},
    {"name": "Іван", "age": 22, "faculty": "ІТ"},
    {"name": "Марія", "age": 19, "faculty": "КН"},
    {"name": "Анна", "age": 23, "faculty": "ІТ"},
    {"name": "Сергій", "age": 24, "faculty": "ФМ"}
]
JSONEOF
        run_program || exit 1
        check_stdout "Олена|Петро|Сергій"
        ;;
esac

exit $?
