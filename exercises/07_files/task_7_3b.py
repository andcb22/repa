# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('CAM_table.txt','r') as f:
    line_list=[]
    for line in f:
        line=line.strip()
        if line and line.split()[0][0].isdigit():
            line_list.append([int(line.split()[0]), line.split()[1], line.split()[3]]) 
    line_list.sort()
#    for line in line_list:
#        print('{:<8}{:20}{}'.format(line[0],line[1],line[2]))
vlan = input('Enter VLAN number: ')
for line in line_list:
    if vlan == line[0]
        print('{:<8}{:20}{}'.format(line[0],line[1],line[2]))



