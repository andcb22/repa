# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
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

def generate_description_from_cdp(filename):
    with open(filename) as f:
        conn_dict={}
        for line in f:
            if line:
                match=re.search(r'(?P<DEV>[a-zA-Z]+\d+)\s+(?P<PRTL>Eth\s\d+/\d+)\s+.+(?P<PRTO>Eth\s\d+/\d+)',line)
                if match:
                    conn_dict[match.group('PRTL')]='description Connected to ' + match.group('DEV') + ' port ' + match.group('PRTO')
            
    pass
    return(conn_dict)


if __name__ == "__main__":
    print("Starting...")
#filename='config_r1.txt'
    filename='sh_cdp_n_sw1.txt'
#    result=get_ints_without_description(filename)
    result=generate_description_from_cdp(filename)
    if result:
       print(result)
    else:
        print('...nothing...')

