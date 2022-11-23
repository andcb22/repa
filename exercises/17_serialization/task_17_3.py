# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re

def parse_sh_cdp_neighbors(file_output):
    for line in file_output.split('\n'):
        match=re.search(r'(\S+)>show cdp neighbors',line)
        if match:
            switchname=match.group(1)
        match=re.search(r'Device ID.+',line)
        if match:
            top_dict={}
        match = re.search(r'(?P<DEV>\S+)\s+(?P<LINT>\S+\s+\S+)\s+(\d+)\s+.+\s+(\S+)\s+(?P<RINT>\S+\s+\S+)',line)
        if match:
            top_dict[match.group('LINT')]={match.group('DEV'):match.group('RINT')}
    return({switchname:top_dict})


if __name__ == "__main__":
    filename='sh_cdp_n_sw1.txt'
    with open(filename, 'r') as fr:
        file_output=fr.read()
        print(parse_sh_cdp_neighbors(file_output))
