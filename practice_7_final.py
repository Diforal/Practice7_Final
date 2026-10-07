"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))
with open(INPUT_FILE) as f:
    (next(f))
    students = 0
    grades1 = 0
    grades2 = 0
    grades3 = 0
    gradess = {}
    named = {}
    for line in f:
        lin = line.strip()
        name, grade1, grade2, grade3 = line.split(",")
        grade1n = int(grade1)
        grade2n = int(grade2)
        grade3n = int(grade3)
        gradess = (grade1n + grade2n + grade3n) / 3
        named[name] = gradess
        grades1 += grade1n
        grades2 += grade2n
        grades3 += grade3n
        students += 1
    best = max(named, key = named.get)
    grades1n = grades1/560
    grades2n = grades2/560
    grades3n = grades3/560
with open(OUTPUT_FILE, "w") as f:
    f.write(f"Середній бал по класу:\n math: {round(grade1n, 1)}\n python: {round(grades2n, 1)}\n java: {round(grades3n, 1)}\n\n Найкращий студент: {name}, ({named[best]})")
    print(f"Середній бал по класу:\n math: {round(grade1n, 1)}\n python: {round(grades2n, 1)}\n java: {round(grades3n, 1)}\n\n Найкращий студент: {name}, ({named[best]})")




# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
