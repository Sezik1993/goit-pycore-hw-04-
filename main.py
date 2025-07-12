# 1 task 

# def total_salary(path):
#     try:
#         with open(path, encoding='utf-8') as file:
#             lines = file.readlines()
#     except FileNotFoundError:
#         print(f"Файл за шляхом '{path}' не знайдено.")
#         return None, None
#     except Exception as e:
#         print(f"Сталася помилка при відкритті файлу: {e}")
#         return None, None
    
#     total = 0
#     count = 0

#     for line in lines:
#         parts = line.strip().split(",")
#         try:
#             salary = int(parts[1])
#         except (IndexError, ValueError):
#             print(f"Некоректний рядок: {line.strip()}")
#             continue
        
#         total += salary
#         count += 1

#     average = total / count if count > 0 else 0
#     return total, average

# total, average = total_salary('salaries.txt')
# if total is not None:
#     print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
 


# 2 task
     
# def get_cats_info(path):
#     cats_list = [] 
#     try:
#         with open(path, 'r', encoding='utf-8') as file:
#             for line in file:
#                 line = line.strip()
#                 if not line:
#                     continue
#                 cat_id, name, age = line.split(',')
#                 cat_info = {
#                     "id": cat_id,
#                     "name": name,
#                     "age": age
#                 }
#                 cats_list.append(cat_info)
#         return cats_list
 
#     except FileNotFoundError:
#         return []
#     except Exception:
#         return []
 
# cats_info = get_cats_info("cats.txt")
# print(cats_info)

# 3 task 

# python --version (v. 3.13.3)
















# Налаштування середовища в терміналі
    # python3 -m venv .env
    # source .env/bin/activate
    # pip install colorama

# def get_info_cats(path):
#     with open(path, "r", encoding="utf-8") as file:
        # id , name , age = ()