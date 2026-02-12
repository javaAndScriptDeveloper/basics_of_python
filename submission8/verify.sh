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

echo "🔍 Verifying submission 8, variant $VARIANT..."

# Check that OOP is used (class keyword present)
if ! grep -q "class " main.py; then
    echo "❌ FAIL: main.py must use OOP (no 'class' keyword found)."
    exit 1
fi
echo "✅ OOP check: 'class' keyword found in main.py."

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
        # Клас для студентів: ім'я та прізвище
        run_test "Олена\nІванова" "[Оо]лена.*[Іі]ванова" || exit 1
        run_test "Петро\nШевченко" "[Пп]етро.*[Шш]евченко"
        ;;
    2)
        # Клас з оцінками та середнім балом
        run_test "3\n5\n4\n3" "[Сс]ередн.*4|4\.0|4,0|: 4" || exit 1
        run_test "2\n5\n5" "[Сс]ередн.*5|5\.0|5,0|: 5"
        ;;
    3)
        # Клас для обчислення віку за роком народження
        run_test "2000" "[Вв]ік.*2[0-9]|2[0-9].*рок" || exit 1
        run_test "1990" "[Вв]ік.*3[0-9]|3[0-9].*рок"
        ;;
    4)
        # Клас студентів з додаванням оцінок у список
        run_test "Олена\n3\n5\n4\n3" "5.*4.*3|[Оо]цінк.*5.*4.*3" || exit 1
        run_test "Петро\n2\n4\n5" "4.*5|[Оо]цінк.*4.*5"
        ;;
    5)
        # Клас бібліотеки: додавання, видалення, перегляд
        run_test "Кобзар\nЕнеїда" "[Кк]обзар.*[Ее]неїда|[Ее]неїда.*[Кк]обзар" || exit 1
        run_test "Кобзар\nЕнеїда" "[Бб]ібліотек|[Кк]ниг"
        ;;
    6)
        # Клас покупки з обчисленням загальної вартості
        run_test "2\nХліб\n25\nМолоко\n30" "55|[Зз]агальн.*55|[Вв]артіст.*55" || exit 1
        run_test "1\nСік\n45" "45|[Зз]агальн.*45|[Вв]артіст.*45"
        ;;
    7)
        # Клас особистих даних співробітників
        run_test "Іванов\nІван\n30\nІнженер" "[Іі]ванов.*[Іі]ван|[Іі]ван.*[Іі]ванов" || exit 1
        run_test "Петренко\nОлена\n25\nМенеджер" "[Пп]етренко.*[Оо]лена|[Оо]лена.*[Пп]етренко"
        ;;
    8)
        # Клас прямокутника: площа та периметр
        run_test "5\n3" "[Пп]лощ.*15|15" || exit 1
        run_test "5\n3" "[Пп]ериметр.*16|16"
        ;;
    9)
        # Клас для записів у календарі
        run_test "15.01.2026\nЗустріч" "15.*01.*2026.*[Зз]устріч|[Зз]устріч.*15" || exit 1
        run_test "20.03.2026\nКонференція" "20.*03.*2026.*[Кк]онференці|[Кк]онференці.*20"
        ;;
    10)
        # Клас для середнього значення групи оцінок
        run_test "5\n5\n4\n3\n5\n3" "[Сс]ередн.*4|4\.0|4,0|: 4" || exit 1
        run_test "3\n4\n5\n3" "[Сс]ередн.*4|4\.0|4,0|: 4"
        ;;
esac

exit $?
