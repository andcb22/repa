# -*- coding: utf-8 -*-
"""
Задание 15.2a

Создать функцию convert_to_dict, которая ожидает два аргумента:
• список с названиями полей
• список кортежей со значениями
Функция возвращает результат в виде списка словарей, где ключи - взяты из первого списка,
а значения подставлены из второго.
Например, если функции передать как аргументы список headers и список
[("R1", "12.4(24)T1", "Cisco 3825"),
("R2", "15.2(2)T1", "Cisco 2911")]
Функция должна вернуть такой список со словарями:
[{"hostname": "R1", "ios": "12.4(24)T1", "platform": "Cisco 3825"},
{"hostname": "R2", "ios": "15.2(2)T1", "platform": "Cisco 2911"}]
Функция не должна быть привязана к конкретным данным или количеству заголов-
ков/данных в кортежах.
Проверить работу функции:
• первый аргумент - список headers
• второй аргумент - список data
Ограничение: Все задания надо выполнять используя только пройденные темы.
headers = ["hostname", "ios", "platform"]
data = [
("R1", "12.4(24)T1", "Cisco 3825"),
("R2", "15.2(2)T1", "Cisco 2911"),
("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
]


"""
import re

filename="sh_ip_int_br.txt"
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
#        print(data_string)
        for header in headers:
#            print(header)
#            print(headers.index(header))
#            print(data_string[headers.index(header)])
            data_dict[header]=data_string[headers.index(header)]
        data_list.append(data_dict)
        data_dict={}
    return(data_list)



def parse_sh_ip_int_br(filename):
    int_list=[]
    intf=()
   #regex=(r'^(?P<INT>[a-zA-Z0-9/]+\d+)\s+(?P<IP>\S+)\s+(\w+)\s+(\w+)\s+(administratively\s)*(?P<STATUS>up|down)\s+(?P<PROT>\S+)')
    regex=(r'^(?P<INT>[a-zA-Z0-9/]+\d+)\s+(?P<IP>\S+)\s+(\w+)\s+(\w+)\s+(?P<STATUS>(administratively\s)*(up|down))\s+(?P<PROT>\S+)')
    with open(filename) as f:
        for line in f:
#            ttttt(line)
            match = re.search(regex,line)
            if match:
#print(match.group('INT')+' '+match.group('IP')+' '+match.group('STATUS')+' '+match.group('PROT'))
                intf=(match.group('INT'),match.group('IP'),match.group('STATUS'),match.group('PROT'))
                int_list.append(intf)
    return(int_list)

#result = parse_sh_ip_int_br(filename)
result = convert_to_dict(headers, data)
if result:
   print(result)
else:
   print('...nothing...')

