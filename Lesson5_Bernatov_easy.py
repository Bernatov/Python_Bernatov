# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil

print('содрежимое папки до преобразований \n\n', os.listdir(), '\n')
for i in range(1, 11): os.mkdir('dir_{}'.format(i))

print('содрежимое папки после преобразований \n\n', os.listdir(), '\n')

for i in range(1, 11):
    os.rmdir('dir_{}'.format(i))
print('содрежимое папки до преобразований \n\n', os.listdir(), '\n')
print(os.getcwd(), '\n')
print(os.listdir()[0], '\n')
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
dir_path = os.path.join(os.getcwd(), 'copy')
try:
    os.mkdir(dir_path)
except FileExistsError:
    print('Такая директория уже существует. Внимание я положу туда файл!')

shutil.copy('{}'.format(os.listdir()[1]), '{}\copy'.format(os.getcwd()))
print('проверка созадания копии файла в папке {} -->'.format(dir_path), os.listdir(dir_path))
