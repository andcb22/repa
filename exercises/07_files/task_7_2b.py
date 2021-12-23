# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
from sys import argv
with open(argv[1],'r') as f_in, open(argv[2],'w') as f_out:
    for line in f_in:
        if line and not line.startswith('!'):
            linec = line.rstrip('\n').split()
            ignored = False
            for item in ignore:
                for word in linec:
                    if word == item:
                        ignored = True
            if not ignored:
                f_out.write(line)

