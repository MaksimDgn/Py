import os

path = os.getcwd()
print("Текущая директория: "+path)
print("Текущая директория: %s" %path)

#os.mkdir("ttt")

path="temp"

try:
    os.mkdir(path)
except OSError:
    print("Создание директонии %s не удалось" %path)
else:
    print("Успешно создана директория %s" %path)