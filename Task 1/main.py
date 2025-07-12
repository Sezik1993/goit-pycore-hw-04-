
def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return None, None
    except Exception as e:
        print(f"Сталася помилка при відкритті файлу: {e}")
        return None, None
    
    total = 0
    count = 0

    for line in lines:
        parts = line.strip().split(",")
        try:
            salary = int(parts[1])
        except (IndexError, ValueError):
            print(f"Некоректний рядок: {line.strip()}")
            continue
        
        total += salary
        count += 1

    average = total / count if count > 0 else 0
    return total, average

total, average = total_salary('salaries.txt')
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
 