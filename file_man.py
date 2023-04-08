import random
import os
import shutil
import sys
import bank
import vicory


# os.rmdir()
# os.rmdir()
# shutil.copy()
# os.listdir()
# os.path.isdir()
# os.path.isfile()
# sys.platform
# print("Ageev Aleksandr")
# Викторина
# Управление счетом
# os.chdir()
# Выход из программы

def file_manege():
    while True:
        answer = int(input(
            f'Выберите действие : \n 1. создать папку \n 2. удалить (файл/папку) \n 3. копировать (файл/папку) \n 4. просмотр содержимого рабочей директории \n 5. посмотреть только папки \n 6. посмотреть только файлы \n 7. просмотр информации об операционной системе \n 8. создатель программы \n 9. играть в викторин \n 10. мой банковский счет \n 11. смена рабочей директории \n 12. выход \n'))

        if answer == 1:
            dir_file = int(input('1.Создать Файл \n2.Создать Папку \n  '))
            if dir_file == 1:
                mkfile = input(f'Введите название папки которую хотите создать \n')
                open(mkfile, 'w')
            elif dir_file == 2:
                mkdir = input(f'Введите название папки которую хотите создать \n')
                os.mkdir(mkdir)
            print(os.listdir())
        elif answer == 2:
            print(os.listdir())
            rmdir = input('Введите название папки которую хотите удалить \n')
            if os.path.isdir(rmdir):
                os.rmdir(rmdir)
            else:
                os.remove(rmdir)
        elif answer == 3:
            cpfile = input('Введите файл или папку для копирования \n')
            namefile = input('Введите новое название файла или папки \n')
            shutil.copy(cpfile, namefile)
            print(os.listdir())
        elif answer == 4:
            print(os.listdir())
        elif answer == 5:
            dirs = []
            for i in os.listdir():
                if os.path.isdir(i) == True:
                    dirs.append(i)
            print(dirs)
        elif answer == 6:
            files = []
            for i in os.listdir():
                if os.path.isfile(i) == True:
                    files.append(i)
            print(files)
        elif answer == 7:
            print(sys.platform)
        elif answer == 8:
            print('Ageev Alexandr')
        elif answer == 9:
            ptr = int(input('Введите , сколько вы хотите сыграть партий:\n'))
            vicory.victory(ptr)
        elif answer == 10:
            bank.bank()
        elif answer == 11:
            der = input('Введите путь до дерриктории или введите .. , чтобы перейти на уровень выше\n')
            os.chdir(der)
        elif answer == 12:
            break
        else:
            print('Введенные данные должны быть числом от 1 - 12')

file_manege()