# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
from sys import argv
with open(argv[1],'r') as f:
    for line in f:
        if line and not line.startswith('!'):
            linec = line.rstrip('\n').split()
            ignored = False
            for item in ignore:
                for word in linec:
                    if word == item:
                        ignored = True
#      print('Ignored!')
#                        print(item)
#                        print(linec)
            if not ignored:
#                print('Not ignored!')
                print(line.rstrip('\n'))

