# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re

#filename="sh_ip_int_br.txt"
filename="cisco_nat_config.txt"
filename_out="cisco_asa_config.txt"
data = [
("R1", "12.4(24)T1", "Cisco 3825"),
("R2", "15.2(2)T1", "Cisco 2911"),
("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
]
headers = ["hostname", "ios", "platform"]

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
#                print(line)
                match = re.search(regex,line.rstrip())
                if match:
#                    print(match.group('IP')) 
#                    print(match.group('PIN')) 
#                    print(match.group('POUT')) 
#                    print(template.format(match.group('IP'),match.group('IP'),match.group('PIN'),match.group('POUT')))
                    f_out.write(template.format(match.group('IP'),match.group('IP'),match.group('PIN'),match.group('POUT')))
    pass



if __name__ == "__main__":

#result = parse_sh_ip_int_br(filename)
#result = convert_to_dict(headers, data)
#if result:
#   print(result)
#else:
#   print('...nothing...')
    print('Starting main...')
    convert_ios_nat_to_asa(filename,filename_out)
