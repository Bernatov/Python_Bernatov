import re

name = input('Введите имя')
surname = input('Введите фамилию')
email = input('Введите email')
result_name_surname = '[a-zа-я]'
result_email = '([a-z0-9_]+@[a-z]+\.(com|ru|org))'

print((re.findall(r'\w+', name)[0] if re.match(result_name_surname, name) == None else 'Введите имя корректно'))
print((re.findall(r'\w+', surname)[0] if re.match(result_name_surname, surname) == None else 'Введите имя корректно'))

try:
    print(re.search(result_email, email).group(1))
except AttributeError:
    print('Введите почту корректно')

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче. погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь. ?
Скользя по утреннему снегу,
Друг милый, предадимся бегу..
Нетерпеливого.... коня
И навестим поля пустые,
Леса, недавно столь густые...,
И берег, милый для меня.'''

try:
    result = '([а-яА-Я]+\.{2,})'
    print('Смотрите что я нашел в тексте:', re.findall(result, some_str))
except AttributeError:  # Тип перехватываемого исключения
    print('Мне жаль, но в тексте нет двух и более точек')
