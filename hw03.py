from pathlib import Path
from colorama import Fore, Style, init
import sys

init()

def print_directory_tree(path: Path, level=0):
    if not path.exists():
        print(Fore.RED + f"Помилка: шлях '{path}' не існує." + Style.RESET_ALL)
        return
    
    if path.is_file():
        print("  " * level + Fore.GREEN + path.name + Style.RESET_ALL)
    else:
        print("  " * level + Fore.BLUE + path.name + "/" + Style.RESET_ALL)
        for item in sorted(path.iterdir()):
            print_directory_tree(item, level + 1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: не передано шлях до директорії." + Style.RESET_ALL)
        print("Приклад запуску: python hw03.py /шлях/до/папки")
    else:
        directory_path = Path(sys.argv[1])
        print_directory_tree(directory_path)
