def get_cats_info(path):
    cats_list = [] 
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                cat_id, name, age = line.split(',')
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_list.append(cat_info)
        return cats_list
 
    except FileNotFoundError:
        return []
    except Exception:
        return []
 
cats_info = get_cats_info("cats.txt")
print(cats_info)

def get_info_cats(path):
    with open(path, "r", encoding="utf-8") as file:
        id , name , age = ()