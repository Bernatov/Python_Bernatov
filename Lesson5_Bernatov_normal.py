import os
import shutil


def del_folder():
    folders_contents()
    del_answer = input('какую папку удалить?')
    try:
        shutil.rmtree(del_answer)
        print('Папка {} успешно удалена'.format(del_answer))
    except FileNotFoundError:
        print('Папки {} не существует'.format(del_answer))


def create_new_folder():
    name_new_folder = input('Введите название создаваемой папки: ')
    new_folder = os.path.join(os.getcwd(), name_new_folder)
    try:
        os.mkdir(new_folder)
        print('Папка {} успешно создана'.format(name_new_folder))
    except FileExistsError:
        print('Папка {} уже существует'.format(name_new_folder))


def folders_contents():
    list_dir = os.listdir()
    for _ in list_dir:
        print(_, '\n')

def change_folder():
    folders_contents()
    change_answer = input('В какую папку перейти?')
    try:
        os.chdir(change_answer)
        print('Переход в папку {} успешно сделан. Вот что в ней находится: '.format(change_answer))
        folders_contents()
    except FileExistsError:
        print('Переход в папку {} не возможен'.format(change_answer))

def start():
    answer = int(input('Воспользуйтесь нашей утилитой\n'
                            'Выберите пункт:\n'
                                '1. Пеерейти в папку\n'
                                '2. просмотреть содержимое текущей папки\n'
                                '3. Удалить папку\n'
                                '4. Созадать папку\n'
                                '---------------------\n'
                                'Ваш выбор номер опции: '))
    if answer == 1:
        change_folder()
    elif answer == 2:
        folders_contents()
    elif  answer ==3:
        del_folder()
    elif answer == 4:
        create_new_folder()
start()