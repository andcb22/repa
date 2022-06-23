# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re

def convert_to_dict(headers, data):
    data_list=[]
    data_dict={}
    for data_string in data:
        for header in headers:
            data_dict[header]=data_string[headers.index(header)]
        data_list.append(data_dict)
        data_dict={}
    return(data_list)

def parse_sh_ip_int_br(filename):
    int_list=[]
    intf=()
    regex=(r'^(?P<INT>[a-zA-Z0-9/]+\d+)\s+(?P<IP>\S+)\s+(\w+)\s+(\w+)\s+(?P<STATUS>(administratively\s)*(up|down))\s+(?P<PROT>\S+)')
    with open(filename) as f:
        for line in f:
            match = re.search(regex,line)
            if match:
                intf=(match.group('INT'),match.group('IP'),match.group('STATUS'),match.group('PROT'))
                int_list.append(intf)
    return(int_list)

def convert_ios_nat_to_asa(filename,filename_out):
    print('startinf func...')
    template='''object network LOCAL_{}
 host {}
 nat (inside,outside) static interface service tcp {} {}
'''
    regex=(r'^ip nat inside source static tcp (?P<IP>\S+)\s+(?P<PIN>\d+)\s.+\s(?P<POUT>\d+)$')
    with open(filename) as f:
        with open(filename_out,'w') as f_out:
            for line in f:
                match = re.search(regex,line.rstrip())
                if match:
                    f_out.write(template.format(match.group('IP'),match.group('IP'),match.group('PIN'),match.group('POUT')))
    pass

def get_ints_without_description(filename):
    int_list=[]
    with open(filename) as f:
        for line in f:
            if line.startswith('interface'):
                match=re.search(r'interface (?P<INT>[a-zA-Z0-9/]+\d+.*\d*)',line)
                if match:
                    int_list.append(match.group('INT'))
            if line.startswith(' description'):
                int_list.pop(-1)
    pass
    return(int_list)


if __name__ == "__main__":
    print("Starting...")
    filename='config_r1.txt'
    result=get_ints_without_description(filename)
    if result:
       print(result)
    else:
        print('...nothing...')


