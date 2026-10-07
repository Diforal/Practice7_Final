"""
Є текстовий файл notes.txt з кількома рядками нотаток.
Потрібно порахувати:
1. скільки всього рядків у файлі;
2. скільки слів у файлі (сумарно по всіх рядках).

Підказка: readlines() тут доречний, бо файл маленький
(на відміну від великих CSV-файлів, де краще йти по рядку за раз).
"""

# TODO 1: відкрийте notes.txt через with open(...) as f: і прочитайте всі рядки
 # замініть на f.readlines()
with open("notes.txt", "r") as f:
    lines = f.readlines()
    # TODO 2: порахуйте кількість рядків
    line_count = len(lines)
# TODO 3: порахуйте кількість слів (сумарно по всіх рядках)
    word_count = 0
    for word in lines:
        split_word = word.split(" ")
        word_count += len(split_word)




print(f"Кількість рядків: {line_count}")
print(f"Кількість слів: {word_count}")