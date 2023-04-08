import colorama
from colorama import Fore, Back, Style
from colorama import init

print(Fore.RED + 'Pupsik') #меняет цвет текста

print(Back.GREEN + 'Pupsik') #меняет цвет заднего фона

print(Style.DIM + 'and in dim text') #меняет стиль текста

print(Style.RESET_ALL) #обнуляет все изменения

init(autoreset=True) #включает автоматическое обнуление всех изменений
