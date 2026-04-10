# Лабораторна робота №6
# Варіант 1

import json
import pandas as pd

# ================= JSON =================

print("=== JSON ===")

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    print(student)

# Додаємо нового студента
students.append({"ім'я": "Анна", "вік": 22, "факультет": "Медицина"})

with open("students_new.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)


# ================= CSV =================

print("\n=== CSV ===")

df_csv = pd.read_csv("data.csv")
print(df_csv)

# Додаємо рядок
df_csv.loc[len(df_csv)] = ["Anna", 22]

df_csv.to_csv("data_new.csv", index=False)


# ================= EXCEL =================

print("\n=== EXCEL ===")

df_excel = pd.read_excel("students.xlsx")
print(df_excel)

# Фільтрація
filtered = df_excel[df_excel["Вік"] > 20]

filtered.to_excel("students_filtered.xlsx", index=False)