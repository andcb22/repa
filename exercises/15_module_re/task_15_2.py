# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re

filename="sh_ip_int_br.txt"

def parse_sh_ip_int_br(filename):
    int_list=[]
    intf=()
   #regex=(r'^(?P<INT>[a-zA-Z0-9/]+\d+)\s+(?P<IP>\S+)\s+(\w+)\s+(\w+)\s+(administratively\s)*(?P<STATUS>up|down)\s+(?P<PROT>\S+)')
    regex=(r'^(?P<INT>[a-zA-Z0-9/]+\d+)\s+(?P<IP>\S+)\s+(\w+)\s+(\w+)\s+(?P<STATUS>(administratively\s)*(up|down))\s+(?P<PROT>\S+)')
    with open(filename) as f:
        for line in f:
#            print(line)
            match = re.search(regex,line)
            if match:
#print(match.group('INT')+' '+match.group('IP')+' '+match.group('STATUS')+' '+match.group('PROT'))
                intf=(match.group('INT'),match.group('IP'),match.group('STATUS'),match.group('PROT'))
                int_list.append(intf)
    return(int_list)

result = parse_sh_ip_int_br(filename)
if result:
   print(result)
else:
   print('...nothing...')

